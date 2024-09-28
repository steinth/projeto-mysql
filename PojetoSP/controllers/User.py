from flask import request, make_response, jsonify, render_template, Blueprint, redirect, url_for
from service.User import atualizarUsuarioService, salvarUsuarioService, listarTodosUsuariosService, removerUmUsuarioService


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
    return redirect(url_for('blueprint.pagina_de_navegacao'))


def listarTodosUsuarios():
    '''
    endpoint: .../usuarios
    metodo: GET
    '''
    pacientes = listarTodosUsuariosService()
    return render_template('lista_pacientes.html', pacientes=pacientes)


def removerUmUsuario(id):
    '''
    endpoint: .../usuario/<int:id>
    metodo: DELETE
    '''
    removerUmUsuarioService(id)
    return redirect(url_for('blueprint.pagina_de_navegacao'))


# sem tempo pra fazer uma funcao atualizar 
def atualizarUsuario(id):
    '''
    endpoint .../atualizar/<int:id>
    metodo: UPDATE
    '''
    atualizarUsuarioService(id)
    return redirect(url_for('blueprint.'))
