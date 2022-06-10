from flask import Flask, jsonify, request
import json

app = Flask(__name__)

''' @app.route("/<int:id>")
def register(id):
 return jsonify({"id": id, "nome": "Pedro", "email": "pedrohr98@hotmail.com"})
 '''

''' @app.route("/register", methods = ["POST"])
def register():
    data = request.data
    return data

@app.route("/update-registration", methods = ["PUT"])
def update():
    data = request.data
    return data '''

# Planos: B - Básico | A - Avançado | I - Ilimitado

# Cadastros
records = [

    {   
        "id": 0,
        "nome": "Pedro",
        "email": "pedrohr98@hotmail.com",
        "plano": "A"
     },

    {
        "id": 1,
        "nome": "Anísio",
        "email": "anisio@hotmail.com",
        "plano": "I"
     }

]

# Cadastrar
@app.route("/register", methods=["POST"])
def register():
    register = json.loads(request.data)
    records.append(register)
    return jsonify(register, "Cadastrado com sucesso!")

# Listar todos os cadastros
@app.route("/records", methods=["GET"])
def get_records():
    return jsonify("Cadastros: ", records)

# Listar um cadastro específico
@app.route("/registration/<int:id>", methods=["GET"])
def get_registration(id):
    try:
        registration = records[id]
        return jsonify("Dados cadastrados: ", registration)
    except IndexError:
        return jsonify("Cadastro não encontrado!")

# Atualizar um cadastro
@app.route("/update-registration/<int:id>", methods=["PUT"])
def update_registration(id):
    try:
        update = json.loads(request.data)
        records[id] = update
        return jsonify(update, "Cadastro atualizado com sucesso!")
    except IndexError:
        return jsonify("Cadastro não encontrado!")

# Excluir um cadastro
@app.route("/delete-registration/<int:id>", methods=["DELETE"])
def delete_registration(id):
    records.pop(id)
    return jsonify("Cadastro excluído com sucesso!")


if __name__ == "__main__":
    app.run(debug=True)
