from flask import render_template
import requests, json
from app.categorias import bp

@bp.route("/")
def index():
    posts=requests.get("https://jsonplaceholder.typicode.com/posts").json()
    usuarios=[]
    x = 1
    cant = 0
    for post in posts:
        cant = cant +1
        if post['userId'] != x:
            usuarios.append({'id': x, 'cantidad':cant})
            x= x+1
            cant =0

    return render_template("categorias/index.html", usuarios=usuarios)

