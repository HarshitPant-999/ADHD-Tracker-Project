from flask import Flask, render_template
from routes.entries import entries_bp
from models import db, Entry
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config["SECRET_KEY"] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.register_blueprint(entries_bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adhd_entries.db'
db.init_app(app)
Bootstrap5(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
