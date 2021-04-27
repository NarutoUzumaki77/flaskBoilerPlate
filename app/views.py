from app import app
from flask import render_template, request, jsonify, redirect, url_for


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/admin/dashboard")
def admin_dashboard():
    return "Hello oh"


@app.route("/comments", methods=["POST"])
def create_comment():
    req = request.get_json()
    
    print(req)

    redirect(request.url)

    return jsonify({"message": "JSON received"}), 200

