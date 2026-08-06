# ADHD Tracker

A small Flask app I built to answer one question I kept asking myself: *when do I actually crash during the day, and what sets it off?*

Not a habit tracker. Not a streak app. Just a place to log the moment — the dopamine-crash, the irritation, the "I can't focus anymore" feeling — and, once I've come back from it, what actually helped.

## Why this exists

I don't do well with vague self-tracking. Writing "had a rough afternoon" in a notes app never told me anything useful a week later. So this app is built around one small idea: split the *crash* from the *recovery*, because they don't happen at the same time, and pretending they do just means the form never gets filled out honestly.

- **Log a crash** the moment it happens — just the time and what you think triggered it. Fast, minimal, because mid-crash is not when you want to fill out a long form.
- **Resolve it later** — once you've actually recovered — with what helped and how long it took.
- **Look back** and see it grouped by day, by time of day, by week. Not to judge it. Just to notice.

## What it actually does right now (v1 / v1.5)

- Log a crash — timestamp + trigger
- Resolve it separately, once you've recovered
- Dashboard: today's count, this week's count, crashes broken down by time-of-day (morning/afternoon/evening/night)
- History: every entry, grouped by day, sub-grouped by time block
- Edit a typo without having to live with it forever
- Unresolved entries just... stay visible as unresolved. That's data too.

## What it deliberately doesn't do

No login. No accounts. No REST API. No React. No AI analysis yet. Not because those ideas are bad — because none of them were solving a real problem I actually had while building this. I kept almost adding them anyway, and kept talking myself back down. That restraint is honestly half the project.

## Stack

Flask, Flask-SQLAlchemy, Flask-WTF, SQLite. Bootswatch (Minty) for styling, because it was free and didn't look terrible on day one.

## Running it locally

```bash
git clone https://github.com/HarshitPant-999/ADHD-Tracker-Project.git
cd ADHD-Tracker-Project
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
flask run
```

No config, no `.env` secrets required for v1 — it's all local SQLite.

## Where this is going (maybe)

If I keep using this for real and something genuinely starts to hurt — I can't find an old entry, I want to check it from my phone, I have enough data to actually want AI to look for patterns in it — that's when auth, an API, or analysis features earn their place. Not before.

## Why I built it this way

I have ADHD, weak working memory, and a habit of over-planning things I've never actually tried yet. This project was as much about *not* doing that as it was about the code — every feature here got questioned before it got built, and a few good ideas got shelved on purpose because I didn't actually need them yet. If you want the whole messy story of how this got built — the git disaster, the debugging, the back-and-forth with myself about scope — it's in [`adhd_tracker_journey.md`](./adhd_tracker_journey.md).
