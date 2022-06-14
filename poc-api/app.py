from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Planos: B - Básico | A - Avançado | I - Ilimitado

# Cadastros
users = [
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
@app.route("/users", methods=["POST"])
def register():
    register = json.loads(request.data)
    users.append(register)
    return jsonify(register, "Cadastrado com sucesso!")


# Listar todos os cadastros
@app.route("/users", methods=["GET"])
def get_records():
    return jsonify("Cadastros: ", users)


# Listar um cadastro específico
@app.route("/users/<int:id>", methods=["GET"])
def get_registration(id):
    try:
        registration = users[id]
        return jsonify("Dados cadastrados: ", registration)
    except IndexError:
        return jsonify("Cadastro não encontrado!")


# Atualizar um cadastro
@app.route("/users/<int:id>", methods=["PUT"])
def update_registration(id):
    try:
        update = json.loads(request.data)
        users[id] = update
        return jsonify(update, "Cadastro atualizado com sucesso!")
    except IndexError:
        return jsonify("Cadastro não encontrado!")


# Excluir um cadastro
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_registration(id):
    users.pop(id)
    return jsonify("Cadastro excluído com sucesso!")


if __name__ == "__main__":
    app.run(debug=True)
