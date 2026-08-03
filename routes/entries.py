from flask import Blueprint, render_template, request, redirect, url_for
from forms import EntryForm, ResolveForm
from models import Entry, db
from datetime import datetime, timedelta

def get_time_block(dt):
    hour = dt.hour
    if hour < 10:
        return "Morning"
    elif hour < 15:
        return "Afternoon"
    elif hour < 19:
        return "Evening"
    else:
        return "Night"

today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

today_start = today
tomorrow_start = today + timedelta(days=1)

entries_bp = Blueprint("entries", __name__)

@entries_bp.route("/log", methods=["GET", "POST"])
def log_entry():
    form = EntryForm()
    if form.validate_on_submit():
        user_data = Entry(
            timestamp = form.timestamp.data,
            trigger = form.trigger.data)
        print(form.timestamp.data)
        db.session.add(user_data)
        db.session.commit()
        return redirect(url_for("entries.resolve", entry_id=user_data.id))
    return render_template("log_entry.html", form=form)

@entries_bp.route("/resolve/<int:entry_id>", methods=["GET", "POST"])
def resolve(entry_id):
    form = ResolveForm()
    log_to_update = db.get_or_404(Entry, entry_id)
    if form.validate_on_submit():
        log_to_update.reset_info = form.reset_info.data
        log_to_update.reset_time = form.reset_time.data
        db.session.commit()
        return redirect(url_for("entries.log_entry"))
    return render_template("resolve.html", form=form)

@entries_bp.route("/dashboard")
def dashboard():
    crashes_today = db.session.execute(
    db.select(db.func.count()).select_from(Entry).where(
        Entry.timestamp >= today_start,
        Entry.timestamp < tomorrow_start
        )).scalar()
    todays_entries = db.session.execute(
    db.select(Entry).where(
        Entry.timestamp >= today_start,
        Entry.timestamp < tomorrow_start
    )).scalars().all()
    return render_template("dashboard.html", crashes_today=crashes_today, entries=todays_entries, get_time_block=get_time_block)

@entries_bp.route("/history")
def history():
    total_entries = db.session.execute(db.select(Entry)).scalars().all()
    total_days = {(entry.timestamp.year, entry.timestamp.month, entry.timestamp.day) for entry in total_entries}
    total_days_count = len(total_days)
    total_entries_count = len(total_entries)
    return render_template("history.html", entries=total_entries, total_crashes=total_entries_count, total_days=total_days_count, get_time_block=get_time_block)


