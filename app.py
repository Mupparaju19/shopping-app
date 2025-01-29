from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Replace with a secure key in production

# Dummy user data (for demonstration only)
users = {
    "admin": {"password": "admin"}
}

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username]["password"] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for("categories"))
        else:
            return "Invalid credentials!"
    return render_template("login.html")

@app.route("/categories")
@login_required
def categories():
    categories = ["Grocery", "Chocolates", "Rice"]
    return render_template("categories.html", categories=categories)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
