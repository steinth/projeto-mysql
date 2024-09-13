from flask import Flask
from main import blueprint
from config import create_table_if_not_exists

app = Flask(__name__)
app.register_blueprint(blueprint)
create_table_if_not_exists()
app.run(host='127.0.0.1', port=8080, debug=True)