from flask import render_template
import requests
from app.post import bp

@bp.route("/")
def index():
    posts=requests.get("https://jsonplaceholder.typicode.com/posts").json()
    return render_template("post/index.html", posts=posts)

@bp.route("/<id>")
def post(id):
    post=requests.get("https://jsonplaceholder.typicode.com/posts/"+id).json()
    return render_template("post/detail.html", post=post, id=id)