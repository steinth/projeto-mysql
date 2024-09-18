from flask import Flask, Blueprint
from controllers.User import salvarUsuario, listarTodosUsuarios, removerUmUsuario

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/cadastro', methods=['GET', 'POST'])(salvarUsuario) # endpoint que chama a função de salvar o usuario    http://localhost:8080/cadastro
blueprint.route('/usuarios', methods=['GET'])(listarTodosUsuarios) # endpoint que chama a função de mostrar todos os usuarios da tabela usuario
blueprint.route('/usuario/<int:id>', methods=['DELETE'])(removerUmUsuario)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
