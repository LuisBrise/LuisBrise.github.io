# Deprecated files: do not run

Kept for reference only. Jekyll does not publish this folder (its name starts with `_`).

| Old files | Use instead | Why |
|---|---|---|
| `talkmap/talkmap.py`, `talkmap/talkmap.ipynb`, `talkmap/talkmap_out.ipynb` | `python3 scripts/update_talkmap.py` | They can overwrite the talk map page and its hand-set coordinates. |
| `cv_json/update_cv_json.sh`, `cv_json/cv_markdown_to_json.py` | Edit `_data/cv.json` directly, keeping it in step with the YAML in `files/CV/_data/cv` (private, not in git) | They rebuild `_data/cv.json` from `_pages/cv.md` and replace the synced data. |
| `markdown_generator/` | The YAML generator in `files/CV/_data` (private, not in git), copying pages into the site without `--clean` | It makes pages from template tables, not from the YAML data. |
