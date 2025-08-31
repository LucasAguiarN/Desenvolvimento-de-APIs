from flask import Flask, jsonify, request

app = Flask(__name__)
lista_usuarios = []
id = 1

# Exibir Todos os Usuários
@app.route('/users', methods=['GET'])
def getUsers():
    return jsonify(lista_usuarios), 200

# Exibir Usuário Especifico
@app.route('/users/<int:user_id>', methods=['GET'])
def getUser(user_id):
    usuario = None
    # Percorrer Lista para Encontrar Usuário pelo ID
    for u in lista_usuarios:
        if u["id"] == user_id:
            usuario = u
            break
    # Se Não Encontrar Usuário
    if usuario is None:
        mensagem = {"Erro": "Usuário não encontrado!"}
        return jsonify(mensagem), 404
    return jsonify(usuario), 200

# Criando Usuário
@app.route('/users', methods=['POST'])
def createUser():
    global id
    dados = request.json
    if not dados:
        return {"Erro": "Requisição deve ser JSON"}, 400
    nome = dados.get("nome")
    email = dados.get("email")
    usuario = {
        "id": id,
        "nome": nome,
        "email": email
    }
    lista_usuarios.append(usuario)
    id += 1
    return jsonify(usuario), 201

# Atualiando Dados do Usuário
@app.route('/users/<int:user_id>', methods=['PUT'])
def updateUser(user_id):
    usuario = None
    # Percorrer Lista para Encontrar Usuário pelo ID
    for u in lista_usuarios:
        if u["id"] == user_id:
            usuario = u
            break
    # Se Não Encontrar Usuário
    if usuario is None:
        mensagem = {"Erro": "Usuário não encontrado!"}
        return jsonify(mensagem), 404
    
    dados = request.json
    if not dados:
        return {"Erro": "Requisição deve ser JSON"}, 400
    nome = dados.get("nome")
    email = dados.get("email")
    usuario["nome"] = nome
    usuario["email"] = email
    return jsonify(usuario), 200

# Excluir Usuário Especifico
@app.route('/users/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    usuario = None
    # Percorrer Lista para Encontrar Usuário pelo ID
    for u in lista_usuarios:
        if u["id"] == user_id:
            usuario = u
            break
    # Se Não Encontrar Usuário
    if usuario is None:
        mensagem = {"Erro": "Usuário não encontrado!"}
        return jsonify(mensagem), 404
    lista_usuarios.remove(usuario)
    mensagem = {"message": "Usuário excluído com sucesso"}
    return jsonify(mensagem), 200

if __name__ == "__main__":
    app.run(debug=True)