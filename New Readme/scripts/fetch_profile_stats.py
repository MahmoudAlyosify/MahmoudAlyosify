"""Fetch public GitHub profile metrics and render a compact SVG dashboard.

This uses the public REST API without a personal token. It intentionally
reports only repository metadata, so the workflow remains safe and portable.
"""
from collections import Counter
from pathlib import Path
import json, os
import requests

USERNAME = os.getenv("GH_USERNAME", "MahmoudAlyosify")
BASE = "https://api.github.com"
HEADERS = {"Accept": "application/vnd.github+json", "User-Agent": "profile-readme-refresh/1.0"}


def get(path, params=None):
    response = requests.get(BASE + path, headers=HEADERS, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def main():
    user = get(f"/users/{USERNAME}")
    repos = get(f"/users/{USERNAME}/repos", {"per_page": 100, "type": "owner", "sort": "updated"})
    languages = Counter(r.get("language") for r in repos if r.get("language"))
    stats = {
        "username": USERNAME,
        "updated": __import__("datetime").date.today().isoformat(),
        "public_repositories": user.get("public_repos", len(repos)),
        "followers": user.get("followers", 0),
        "following": user.get("following", 0),
        "stars": sum(r.get("stargazers_count", 0) for r in repos),
        "forks": sum(r.get("forks_count", 0) for r in repos),
        "top_languages": languages.most_common(5),
    }
    Path("data/profile_stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    rows = [
        ("public repos", stats["public_repositories"]),
        ("followers", stats["followers"]),
        ("stars received", stats["stars"]),
        ("forks", stats["forks"]),
    ]
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 166" role="img" aria-label="Live GitHub profile statistics">',
        '<rect width="860" height="166" rx="12" fill="#0d1117" stroke="#30363d"/>',
        '<text x="35" y="27" fill="#c9d1d9" font-family="monospace" font-size="13">github profile / public signals</text>',
        f'<text x="825" y="27" text-anchor="end" fill="#8b949e" font-family="monospace" font-size="11">updated {stats["updated"]}</text>',
    ]
    for i, (label, value) in enumerate(rows):
        x = 35 + i * 205
        delay = i * 0.12
        parts.append(f'<g opacity="0.18"><rect x="{x}" y="48" width="176" height="76" rx="8" fill="#161b22" stroke="#21262d"/><text x="{x+16}" y="78" fill="#7ee787" font-family="monospace" font-size="25" font-weight="bold">{value:,}</text><text x="{x+16}" y="101" fill="#8b949e" font-family="monospace" font-size="11">{label}</text><animate attributeName="opacity" from="0.18" to="1" dur="0.4s" begin="{delay:.2f}s" fill="freeze"/></g>')
    langs = " · ".join(name for name, _ in stats["top_languages"]) or "metadata pending"
    parts.append(f'<text x="35" y="148" fill="#58a6ff" font-family="monospace" font-size="11">top public languages: {langs}</text>')
    parts.append('</svg>')
    Path("profile-stats.svg").write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote data/profile_stats.json and profile-stats.svg for {USERNAME}")


if __name__ == "__main__":
    main()
