from flask import Blueprint, render_template, request, redirect

entries_bp = Blueprint("entries", __name__)

@entries_bp.route("/log", methods=["GET", "POST"])
def log_entry():
    form = EntryForm()
    if form.validate_on_submit():
        user_data = Entry(
            time = form.timestamp.data,
            trigger = form.trigger.data,
            reset_info = form.reset_info.data,
            reset_time = form.reset_time.data)
        db.session.add(user_data)
        db.session.commit()
    return render_template("log_entry.html", form=form)
