from flask import Flask 
app = Flask(__name__) 
@app.route("/") 
def h_world(): 
    return "<h1>Hello world</h1>"