from flask import Flask, render_template
from routes.entries import entries_bp
from models import Entry

app = Flask(__name__)
app.config["SECRET_KEY"] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.register_blueprint(entries_bp)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")








if __name__ == "__main__":
    app.run(debug=True)
