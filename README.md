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
