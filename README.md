# 🕷️ Scraping Authenticated React Websites with Playwright  
*A real-world case study*

This repository demonstrates **how to reliably scrape modern, React-based websites**
that use component libraries like **Material UI (MUI)** — even when:

- Content is loaded dynamically
- Pagination has no URL parameters
- Sessions require authentication
- DOM structure is inconsistent
- Long-running jobs must be resume-safe

> ⚠️ This project is **educational**.  
> No real credentials, sessions, or scraped datasets are included.

---

## The Problem

Traditional scraping approaches (Requests + BeautifulSoup) fail when:

- Pages are rendered client-side
- Elements appear conditionally
- CSS class names are auto-generated
- Pagination is handled internally by JavaScript
- Sessions expire mid-run

This project documents **how to solve those issues systematically**.

---

## Key Techniques Used

### 1. Session Persistence
- Logged in once using Playwright
- Reused browser context for long-running jobs
- Avoided repeated authentication

### 2. Pagination Without URLs
- Pages shared the same URL
- Pagination buttons were triggered via JS
- Solved using **ARIA labels**, not fragile text selectors

```python
page.locator("button[aria-label='Go to page 2']").click()
```

--- 

### 3. Semantic Selectors Over CSS Hashes

Instead of brittle selectors like:

```css
.css-1anx036
```

We used **semantic intent**:

```python
div.MuiTypography-h6
```

This survives UI rebuilds and class rehashing.

---

### 4. Defensive DOM Access

Real-world pages are inconsistent.

* Some cards miss fields
* Some sections load late
* Some entities have partial data

All extraction logic is wrapped defensively to avoid crashes.

---

### 5. Resume-Safe Data Enrichment

Instead of re-scraping everything:

* Raw IDs were collected first
* Partial datasets were enriched later
* CSV updates were done per-group, not per-row
* Allowed safe restarts after failures

---

## What This Repo Is (and Isn’t)

✅ Focused on **engineering patterns**
✅ Reusable for other React/MUI sites
✅ Recruiter-friendly case study

❌ Not tied to a specific website
❌ No proprietary data
❌ No credentials or sessions

---

## Who This Is For

* Developers scraping modern web apps
* Data engineers dealing with messy UIs
* Students learning Playwright beyond tutorials
* Anyone tired of brittle CSS selectors

---

## Lessons Learned

* ARIA labels are gold for scraping
* Never trust HTML tag semantics in React
* Pandas `NaN` handling matters more than you think
* Scraping is 30% extraction, 70% error handling

---

## Disclaimer

This repository is for **educational purposes only**.
Always respect a website’s terms of service and legal boundaries.
