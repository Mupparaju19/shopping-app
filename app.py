from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "RXzvlRpabTEDq3MJJQMpfeVHzay3Z6"  

# Dummy user data with hashed passwords
users = {
    "admin": {"password": generate_password_hash("admin")}
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
        # Check if the username exists and if the password matches
        if username in users and check_password_hash(users[username]["password"], password):
            user = User(username)
            login_user(user)
            return redirect(url_for("categories"))
        else:
            return "Invalid credentials!"  # Improve with a better message
    return render_template("login.html")

@app.route("/categories")
@login_required
def categories():
    categories = ["Milk", "Rice", "Groceries"]  # Example categories
    return render_template("categories.html", categories=categories)

@app.route("/logout")
@login_required
def logout():
    logout_user()  # Log the user out
    return redirect(url_for("login"))  # Redirect to login page after logout

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
