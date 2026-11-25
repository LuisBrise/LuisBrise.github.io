#!/usr/bin/env python3
"""Regenerate talkmap/org-locations.js from the location fields in _talks/*.md.

Run from anywhere:   python3 scripts/update_talkmap.py

Coordinates are kept in talkmap/locations.json. A location that is not there
yet is looked up once on OpenStreetMap (Nominatim) and saved; only the location
text is sent. Edit locations.json by hand to move a marker. Needs PyYAML only.
Unlike the old tools in _deprecated/talkmap, this does not overwrite talkmap/map.html.
"""
import html
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "talkmap" / "locations.json"
OUT = ROOT / "talkmap" / "org-locations.js"


def geocode(place):
    """Try the full text, then drop leading parts ("Institute, City" -> "City")."""
    parts = [p.strip() for p in place.split(",")]
    for i in range(len(parts)):
        query = urllib.parse.urlencode({"q": ", ".join(parts[i:]), "format": "json", "limit": 1})
        req = urllib.request.Request(
            f"https://nominatim.openstreetmap.org/search?{query}",
            headers={"User-Agent": "academicpages-talkmap"},
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            hits = json.load(r)
        time.sleep(1)  # Nominatim allows one request per second
        if hits:
            if i:
                print(f"  note: used '{', '.join(parts[i:])}' for '{place}'")
            return [round(float(hits[0]["lat"]), 4), round(float(hits[0]["lon"]), 4)]
    return None


def main():
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    points, missing = [], []
    for f in sorted((ROOT / "_talks").glob("*.md")):
        talk = yaml.safe_load(f.read_text(encoding="utf-8").split("---", 2)[1])
        place = str(talk.get("location") or "").strip()
        if not place:
            continue
        if place not in cache:
            print(f"Looking up: {place}")
            try:
                found = geocode(place)
            except OSError as err:
                print(f"  lookup failed: {err}")
                found = None
            if not found:
                missing.append(place)
                continue
            cache[place] = found
        text = f"{html.escape(talk['title'].strip())}<br />{html.escape(str(talk['venue']).strip())}, {html.escape(place)}"
        points.append([text, *cache[place]])

    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT.write_text("var addressPoints = " + json.dumps(points, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")
    print(f"{len(points)} talks written to {OUT.relative_to(ROOT)}")
    if missing:
        sys.exit("Not on the map (add them to talkmap/locations.json): " + "; ".join(missing))


if __name__ == "__main__":
    main()
