# TrendPulse

MASAI learning assignment: a 4-stage Hacker News trend pipeline (collect → clean → analyse → visualise).
Each stage is a standalone top-level script, run in order.

## Pipeline

| Script | Reads | Writes |
|---|---|---|
| `task1_data_collection.py` | HN Firebase API | `data/trends_YYYYMMDD.json` |
| `task2_data_processing.py` | latest `data/trends_*.json` (by ctime) | `data/trends_clean.csv` |
| `task3_analysis.py` | `data/trends_clean.csv` | `data/trends_analysed.csv` |
| `task4_visualization.py` | `data/trends_analysed.csv` | `outputs/*.png` |

## Running

- venv lives in `venv/`. Use `venv\Scripts\python.exe task3_analysis.py` (or activate first) — not bare `python`.
- **Don't re-run task1 unless I ask.** It makes ~100 sequential HTTP calls to the HN API (slow). Existing
  `data/trends_*.json` is fine for testing tasks 2-4.
- `task4_visualization.py` calls `plt.show()`, which blocks waiting for a window close. To run it unattended,
  set `$env:MPLBACKEND='Agg'` first.

## Conventions in this code (keep them)

- Deliberately beginner-style: top-level scripts, `# checkpoint-N` comments, `print()` for progress, no
  functions/classes/logging/try-except wrappers. Don't "improve" this into production structure.
- Column renames happen in task2: `id`→`post_id`, `descendants`→`num_comments`.
- Derived fields (task3): `engagement = num_comments / (score + 1)`, `is_popular = score > mean(score)`.
- Categories come from keyword matching in `assign_category()` — the HN API has no category field.

## Gotchas

- `requirements.txt` and `requirement.txt` are both UTF-16 `pip freeze` dumps and neither is complete:
  `requirements.txt` omits pandas, `requirement.txt` omits matplotlib. Ask before regenerating or consolidating.
- Never commit `venv/`. Regenerated CSVs and `outputs/*.png` only get committed if I ask.
