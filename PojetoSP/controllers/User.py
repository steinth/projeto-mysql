from flask import request, make_response, jsonify, render_template, Blueprint, redirect, url_for
from service.User import atualizarUsuarioService, buscarPorIdService, exibirInformacoesService, salvarUsuarioService, listarTodosUsuariosService, removerUmUsuarioService


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


def exibirInformacoes(id):
    usuario = exibirInformacoesService(id)
    return render_template('informacoesUsuario.html', usuario = usuario)


def atualizarUsuario(id):
#
#    if request.method == 'GET':
#        paciente = buscarPorIdService(id)
#        return render_template('atualizarUsuario.html', paciente=paciente)
#
#    elif request.method == 'PUT':
#        nome = request.form.get('nome')
#        email = request.form.get('email')
#        cpf = request.form.get('cpf')
#        atualizarUsuarioService(id, nome, email, cpf)
#        return redirect(url_for('blueprint.pagina_de_navegacao'))
    pass

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


