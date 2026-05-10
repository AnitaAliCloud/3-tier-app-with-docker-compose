from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend:5000")

@app.route("/")
def index():
    response = requests.get(f"{BACKEND_URL}/api/users")
    users = response.json()
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)