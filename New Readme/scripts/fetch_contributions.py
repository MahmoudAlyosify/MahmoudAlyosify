"""Fetch a public GitHub contribution calendar without a token."""
from __future__ import annotations
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
import json, os, re
import requests
from bs4 import BeautifulSoup

USERNAME = os.getenv("GH_USERNAME", "MahmoudAlyosify")
OUT = Path("data/contributions.json")
URL = f"https://github.com/users/{USERNAME}/contributions"


def main():
    response = requests.get(URL, headers={"User-Agent": "profile-readme-refresh/1.0"}, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    days = []
    for cell in soup.select("td.ContributionCalendar-day[data-date]"):
        raw = cell.get("data-level", "0")
        try: level = int(raw)
        except ValueError: level = 0
        title = cell.get("data-count", "") or cell.get("aria-label", "")
        if not title:
            tip = cell.find_next("tool-tip")
            title = tip.get_text(" ", strip=True) if tip else ""
        count_match = re.search(r"(\d[\d,]*)\s+contribution", title, flags=re.I)
        count = int(count_match.group(1).replace(",", "")) if count_match else 0
        days.append({"date": cell["data-date"], "count": count, "level": max(0, min(level, 5))})
    if not days:
        raise RuntimeError("No contribution cells found; GitHub may have changed its HTML.")
    days = days[-371:]
    counts = [d["count"] for d in days]
    streak = longest = current = 0
    by_day = {date.fromisoformat(d["date"]): d["count"] for d in days}
    cursor = date.today()
    while cursor in by_day and by_day[cursor] > 0:
        current += 1; cursor -= timedelta(days=1)
    run = 0
    for d in days:
        run = run + 1 if d["count"] > 0 else 0
        longest = max(longest, run)
    monthly = defaultdict(int)
    for d in days:
        monthly[d["date"][:7]] += d["count"]
    payload = {"username": USERNAME, "updated": date.today().isoformat(), "days": days,
               "stats": {"total": sum(counts), "current_streak": current,
                          "longest_streak": longest, "best_day": max(counts),
                          "monthly": dict(sorted(monthly.items()))}}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {OUT} ({len(days)} days, {payload['stats']['total']} contributions)")

if __name__ == "__main__": main()
