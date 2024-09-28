from flask import Flask, request
from main import blueprint, create_app
from config import create_table_if_not_exists

app = Flask(__name__)
app.register_blueprint(blueprint)
create_table_if_not_exists()
app.run(host='127.0.0.1', port=8080, debug=True)

if __name__ == '__main__':
    app = create_app()
    app.run()