from flask import Flask, Blueprint, render_template
from controllers.User import  exibirInformacoes, salvarUsuario, listarTodosUsuarios, removerUmUsuario

blueprint = Blueprint('blueprint', __name__)
#http://localhost:8080

def pagina_de_navegacao():
    return render_template('navegacao.html')

blueprint.route('/cadastro', methods=['GET', 'POST'])(salvarUsuario)
blueprint.route('/usuarios', methods=['GET'])(listarTodosUsuarios)
blueprint.route('/usuario/<int:id>', methods=['DELETE', 'POST'])(removerUmUsuario)
blueprint.route('/navegacao', methods=['GET'])(pagina_de_navegacao)
blueprint.route('/informacoes/<int:id>', methods=['GET'])(exibirInformacoes)
#blueprint.route('/atualizar/<int:id>', methods=['GET', 'PUT'])(atualizarUsuario)



def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    return app
