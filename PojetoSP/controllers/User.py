from flask import request, make_response, jsonify
from service.User import salvarUsuarioService, listarTodosUsuariosService, removerUmUsuarioService

def salvarUsuario():
    '''   
    endpoint: .../cadastro
    metodo: POST
    '''
    usuario = request.json
    salvarUsuarioService(usuario)  # Chama o service para processar a lógica de salvar
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