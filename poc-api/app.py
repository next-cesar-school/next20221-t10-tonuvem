from flask import Flask, jsonify, request
import json

app = Flask(__name__)

''' @app.route("/<int:id>")
def register(id):
 return jsonify({"id": id, "nome": "Pedro", "email": "pedrohr98@hotmail.com"})
 '''

@app.route("/register", methods = ["POST"])
def register():
    data = request.data
    return data

@app.route("/update-registration", methods = ["PUT"])
def update():
    data = request.data
    return data

if __name__ == "__main__":
    app.run(debug = True)