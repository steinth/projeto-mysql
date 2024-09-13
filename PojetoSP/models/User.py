from config import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash


def salvarUsuario(usuario):
    """
    Salva um novo usuário no banco de dados.
    Argumentos:
    - usuario: Um dicionário contendo as informações do usuário (email, senha e cpf).
    """
    nome = usuario.get('nome')
    email = usuario.get('email')
    senhaHashed = generate_password_hash(usuario.get('senha'), method='pbkdf2:sha256')
    cpf = usuario.get('cpf')

    # Conexão com o banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Inserção no banco de dados sem criptografia
    cursor.execute(
        'INSERT INTO usuario (nome, email, senha, cpf) VALUES (%s, %s, %s, %s)',
        (nome, email, senhaHashed, cpf)
    )
    conn.commit()  # Confirma a transação
    conn.close()   # Fecha a conexão


def listagemTodosUsuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT id, nome, email, cpf FROM usuario')
    usuario = cursor.fetchall()
    conn.close()
    return usuario


def removerUsuario(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuario WHERE id = %s', (id,))
    conn.commit()
    conn.close()

def atualizarUsuario(id, usuario):
    pass