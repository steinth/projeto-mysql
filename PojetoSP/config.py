#import pymysql                                  #pip install pymysql
import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='usuario',  # usuário MySQL
        password='123',  # senha MySQL
        database='Pacientes'  # nome do banco de dados
    )    


def create_table_if_not_exists():
    conn = get_db_connection()
    if conn is None:
        print("Não foi possível conectar ao banco de dados.")
        return
    
    cursor = conn.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        senha VARCHAR(255) NOT NULL,
        cpf VARCHAR(11) NOT NULL
    );
    """
    
    cursor.execute(create_table_query)
    conn.commit()
    
    cursor.close()
    conn.close()
    print("Tabela criada com sucesso!")
