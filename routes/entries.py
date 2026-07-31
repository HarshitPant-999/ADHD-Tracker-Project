from flask import Blueprint, render_template, request, redirect

entries_bp = Blueprint("entries", __name__)

@entries_bp.route("/log", methods=["GET", "POST"])
def log_entry():
    ...

