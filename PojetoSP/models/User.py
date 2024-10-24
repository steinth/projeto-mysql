from config import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash


def salvarUsuario(nome, email, senha, cpf):
    """
    Salva um novo usuário no banco de dados.
    """

    senhaHashed = generate_password_hash(senha, method='pbkdf2:sha256')

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

def atualizarUmUsuario(id, nome, email, cpf):
    #conn = get_db_connection()
    #cursor = conn.cursor()
    #cursor.execute('UPDATE usuario SET nome = %s, email = %s, cpf = %s WHERE id = %s', (nome, email, cpf, id))
    #conn.commit()
    #conn.close()
    pass

def buscarPorId(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuario WHERE id = %s', (id,))
    paciente = cursor.fetchone()
    conn.close()
    return paciente

def exibirInformacoesUsuario(id):
#    conn = get_db_connection()
#    cursor = conn.cursor()
#    cursor.execute('SELECT nome, email, cpf FROM usuario WHERE id = %s',(id))
    pass