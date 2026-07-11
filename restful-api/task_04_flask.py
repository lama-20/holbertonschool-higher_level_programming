#!/usr/bin/python3
"""A simple API built with Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
# NOTE: keep this empty when pushing your code, so the checker
# doesn't encounter unexpected pre-existing data.
users = {}


@app.route("/")
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return the full object for a given username."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the users dictionary."""
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
