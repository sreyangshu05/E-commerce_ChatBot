from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "a3f5c6e7d8e9f0a1b2c3d4e5f6a7b8c9"

# Connect to SQLite database and fetch data
def query_database(query, params=()):
    connection = sqlite3.connect("database/ecommerce.db")
    cursor = connection.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    connection.close()
    return results

# Store chat logs in the database
def log_chat(user_id, message, timestamp):
    connection = sqlite3.connect("database/ecommerce.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO chat_logs (user_id, message, timestamp) VALUES (?, ?, ?)", (user_id, message, timestamp))
    connection.commit()
    connection.close()

# User registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        connection = sqlite3.connect("database/ecommerce.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connection.commit()
        connection.close()
        return redirect(url_for("login"))
    return render_template("register.html")

# User login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        connection = sqlite3.connect("database/ecommerce.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        connection.close()
        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["username"] = user[1]
            return redirect(url_for("index"))
        return "Invalid credentials"
    return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# Chatbot main page
@app.route("/")
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", username=session["username"])

# Search products
@app.route("/search", methods=["GET"])
def search_products():
    if "user_id" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    query = request.args.get("query", "").lower()
    results = query_database("SELECT * FROM products WHERE LOWER(name) LIKE ?", (f"%{query}%",))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_chat(session["user_id"], f"Search query: {query}", timestamp)
    return jsonify(results)

# Fetch all products
@app.route("/products", methods=["GET"])
def fetch_all_products():
    results = query_database("SELECT * FROM products")
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
