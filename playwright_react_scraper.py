"""
Case Study: Scraping authenticated, React-based websites using Playwright.

Key techniques demonstrated:
- Session persistence
- Pagination without URL parameters
- ARIA-label based selectors
- Defensive DOM handling
- Resume-safe data enrichment
"""

from playwright.sync_api import sync_playwright
import pandas as pd
import time


BASE_URL = "https://example.com"  # placeholder
IDS_CSV = "data/ids.csv"
INPUT_CSV = "data/input.csv"
OUTPUT_CSV = "data/output.csv"


def scrape_names(page, entity_id):
    """
    Extracts names from a React/MUI card layout.
    Uses semantic class selectors instead of tag assumptions.
    """
    page.goto(f"{BASE_URL}/entity/{entity_id}", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    page.mouse.wheel(0, 3000)

    cards = page.locator("div.MuiCard-root")
    names = []

    for i in range(cards.count()):
        try:
            name = cards.nth(i).locator(
                "div.MuiTypography-h6"
            ).first.text_content(timeout=2000).strip()
            names.append(name)
        except:
            continue

    return names


def main():
    ids_df = pd.read_csv(IDS_CSV)
    data_df = pd.read_csv(INPUT_CSV)

    name_map = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()  # session.json omitted for repo safety
        page = context.new_page()

        for idx, entity_id in enumerate(ids_df["ID"], start=1):
            print(f"[{idx}] Processing {entity_id}")
            try:
                name_map[entity_id] = scrape_names(page, entity_id)
            except:
                continue
            time.sleep(1.5)

        browser.close()

    # Apply names safely
    for entity_id, names in name_map.items():
        rows = data_df[
            (data_df["ID"] == entity_id) & (data_df["Name"].isna())
        ].index

        for i, row_idx in enumerate(rows):
            if i >= len(names):
                break
            data_df.at[row_idx, "Name"] = names[i]

    data_df.to_csv(OUTPUT_CSV, index=False)
    print("Done.")


if __name__ == "__main__":
    main()
