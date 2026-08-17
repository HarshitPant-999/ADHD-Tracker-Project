# ADHD Tracker

A small Flask app for logging focus/energy crashes — when they happen, what triggered them, and what helped after recovery. Built as a local-first, no-login v1, with an emphasis on keeping the logging step fast enough to actually use in the moment.

## Core design decision: log and resolve are separate steps

The trigger for a crash is known immediately; the recovery details (what helped, how long it took) aren't known until later. Cramming both into one form meant the form couldn't honestly be filled out in real time. So the data model is split across two routes writing to the same row:

- `POST /log` — creates an `Entry` with `timestamp` + `trigger`. `reset_info` / `reset_time` are left `NULL`.
- `POST /resolve/<id>` — fetches that same row and updates `reset_info` / `reset_time` once recovery has happened.

One `Entry` = one full crash-to-recovery cycle, populated across two requests instead of one.

## Features (v1 / v1.5)

- **Log route** (`/log`) — `EntryForm`: `DateTimeLocalField` + `StringField`, creates a row
- **Resolve route** (`/resolve/<id>`) — `ResolveForm`, fetches via `db.get_or_404`, updates in place
- **Edit route** — merged form covering `trigger` + `reset_info`, pre-filled via `EditForm(obj=entry)`, for fixing typos post-hoc
- **Dashboard** (`/dashboard`):
  - Today's crash count — `db.func.count()` with a `timestamp` range filter (`today_start <= ts < tomorrow_start`)
  - Last 7 days' count, same range pattern extended to a week boundary
  - Crashes aggregated by time-of-day across the week (computed via a `time_block` property on `Entry`, tallied in a dict)
- **History** (`/history`) — entries grouped by day, then sub-grouped by time block, via nested Jinja `groupby` filters
- Unresolved entries (`reset_info IS NULL`) are shown as-is with a link to `/resolve/<id>` — no separate "todo list" UI; open state is treated as valid data, not an error state

## Explicitly out of scope for v1

No auth, no REST API (`jsonify`), no JS framework, no AI-driven analysis, no PostgreSQL. Each of these was scoped out because nothing in the current single-user, local-only usage pattern requires them yet — not a permanent decision, just not solving a problem that exists right now.

## Stack

- Flask, Flask-SQLAlchemy (`Mapped`/`mapped_column` style models), Flask-WTF/WTForms
- SQLite (`instance/tracker.db`)
- Jinja templates, Bootswatch (Minty) via CDN — no build step, no bundler
- Blueprint-based route organization (`entries_bp`)

## Running it locally

```bash
git clone https://github.com/HarshitPant-999/ADHD-Tracker-Project.git
cd ADHD-Tracker-Project
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
flask run
```

No config or `.env` secrets required for v1 — SQLite file is created locally via `db.create_all()` inside an app context.

## Notable bugs fixed along the way

- A local variable named `DateTime` shadowed the SQLAlchemy `DateTime` import, causing a misleading `ArgumentError` at `create_all()` far from the actual cause
- `.scalars()` called on a `Select` object instead of on the executed result of `db.session.execute(...)`
- Date-range filtering (`today`/`this week`) required exact half-open boundaries (`>= start`, `< end`) rather than same-day equality checks, which don't work against full `datetime` values
- A `@property` on the model (`time_block`) can't be assigned to directly without a setter — resolved by relying on the property for reads instead of manually setting the attribute in each route
- A git object corruption incident (`fatal: loose object ... is corrupt`) required rebuilding `.git` from `origin/main`; recovered without data loss due to a manual backup taken before running `git reset --hard`

## Possible next steps

Only if a concrete need shows up during real use: multi-device access (→ auth + API), an interactive frontend for specific views (→ JS), or trend analysis once there's enough accumulated data. None of these are planned on a timeline.

## More context

A longer, more narrative writeup of how this was built — decisions, dead ends, and the debugging process — is in [`adhd_tracker_journey.md`](./adhd_tracker_journey.md).

#new change:
 added another log with crash - sleep time last night
