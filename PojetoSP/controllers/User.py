from flask import request, make_response, jsonify, render_template, Blueprint
from service.User import salvarUsuarioService, listarTodosUsuariosService, removerUmUsuarioService


def salvarUsuario():
    '''   
    endpoint: .../cadastro
    metodo: POST
    '''

    if request.method == 'GET':
        # Renderiza o formulário quando for acessado via GET
        return render_template('cadastro.html')
    data = request.form

    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    cpf = data.get('cpf')

    salvarUsuarioService(nome, email, senha, cpf)  # Chama o service para processar a lógica de salvar
    return make_response(jsonify(mensagem="Usuário salvo com sucesso!"), 201)


def listarTodosUsuarios():
    '''
    endpoint: .../usuarios
    metodo: GET
    '''
    return make_response(
        jsonify(mensagem="Lista de usuarios",
                usuario=listarTodosUsuariosService()))


def removerUmUsuario(id):
    '''
    endpoint: .../usuario/<int:id>
    metodo: DELETE
    '''
    removerUmUsuarioService(id)
    return make_response(jsonify(mensagem="Paciente removido com sucesso"))

def atualizarUsuario():
    pass