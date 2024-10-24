from flask import Flask, Blueprint, render_template
from controllers.User import atualizarUsuario, exibirInformacoes, salvarUsuario, listarTodosUsuarios, removerUmUsuario

blueprint = Blueprint('blueprint', __name__)
#http://localhost:8080

def pagina_de_navegacao():
    return render_template('navegacao.html')

blueprint.route('/cadastro', methods=['GET', 'POST'])(salvarUsuario) # endpoint que chama a função de salvar o usuario    http://localhost:8080/cadastro
blueprint.route('/usuarios', methods=['GET'])(listarTodosUsuarios) # endpoint que chama a função de mostrar todos os usuarios da tabela usuario     http://localhost:8080/usuarios
blueprint.route('/usuario/<int:id>', methods=['DELETE', 'POST'])(removerUmUsuario) # endpoint usado para remover um usuario, recebe um id como argumento
blueprint.route('/navegacao', methods=['GET'])(pagina_de_navegacao) #uma pagina com opções de ver a lista de pacientes ou cadastrar um novo paciente
blueprint.route('/informacoes/<int:id>', methods=['GET'])(exibirInformacoes)
#blueprint.route('/atualizar/<int:id>', methods=['GET', 'PUT'])(atualizarUsuario) # endpoint usado para atualizar um usuario, recebe um id como argumento



def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    return app
