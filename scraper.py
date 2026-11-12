import csv
import time
import random
import requests

URL = "https://quotes.toscrape.com/api/quotes"
HEADERS = {"User-Agent": "Mozilla/5.0"}

rows = []
page = 1

while True:
    response = requests.get(URL, params={"page": page}, headers=HEADERS, timeout=10)
    response.raise_for_status()
    data = response.json()

    for quote in data["quotes"]:
        rows.append({
            "author": quote["author"]["name"],
            "text": quote["text"],
            "tags": ", ".join(quote["tags"]),
        })

    if not data["has_next"]:
        break

    page += 1
    time.sleep(random.uniform(1, 2))

with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["author", "text", "tags"])
    writer.writeheader()
    writer.writerows(rows)

print("Saved", len(rows), "quotes")