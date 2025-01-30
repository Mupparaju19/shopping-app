from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "zX1ATENFiqLvaM9aw33rvc67FDFiYn"  

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
            flash("Invalid username or password. Please try again.", "error")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Check if the username already exists
        if username in users:
            flash("Username already exists. Please choose another one.", "error")
            return redirect(url_for("register"))
        
        # Hash the password and store the new user
        hashed_password = generate_password_hash(password)
        users[username] = {"password": hashed_password}
        
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for("login"))
    
    return render_template("register.html")

@app.route("/categories")
@login_required
def categories():
    categories = ["Milk", "Rice", "Groceries"]
    return render_template("categories.html", categories=categories)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out.", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
