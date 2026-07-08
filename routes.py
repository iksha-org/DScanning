from flask import request
from app import app

@app.route("/greet")
def greet():
    name = request.args.get("name", "")
    return f"<h1>Hello {name}</h1>"