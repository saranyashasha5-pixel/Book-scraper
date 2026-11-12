# Quotes API Scraper

A Python scraper that collects quotes from the practice site
[quotes.toscrape.com](https://quotes.toscrape.com/scroll), which is built for
learning web scraping. It reads the site's hidden JSON API instead of parsing HTML.

## What it does
- Calls the hidden API behind the site's infinite scroll (`/api/quotes?page=N`)
- Pages through the results until the API says there is no next page
- Extracts the author, quote text and tags
- Saves everything to `quotes.csv`

## How to run
    pip install -r requirements.txt
    python scraper.py

## Design choices
- **Hidden API over HTML parsing:** found in the browser's Network tab (Fetch/XHR).
  It returns clean JSON, so there is no HTML to parse and it is lighter than
  running a browser.
- **Stop condition:** the loop ends when the response's `has_next` is false,
  so it does not depend on a guessed page count.
- **Polite scraping:** a random 1 to 2 second delay between requests, plus a
  request timeout so one slow response cannot freeze the run.
- **Fails loudly:** `raise_for_status()` stops the script on an error response
  instead of saving bad data.

## Output
`quotes.csv` with the columns `author`, `text` and `tags`.

## Note
This project uses a public practice site made for scraping. For real sites,
check the robots.txt and terms of service first.# Book-scraper
