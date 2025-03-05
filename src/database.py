import sqlite3
import os

def create_table():
    # Cria a pasta 'src' se ela não existir
    os.makedirs('src', exist_ok=True)

    # Define o caminho do banco de dados na pasta 'src'
    db_path = os.path.join('src', 'users.db')

    # Conecta ao banco de dados (cria se não existir)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Apaga a tabela 'users' se ela já existir
    cursor.execute('DROP TABLE IF EXISTS users')

    # Cria a nova tabela com os campos: id, username, password_hash, failed_attempts, locked
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password_hash TEXT,
            failed_attempts INTEGER DEFAULT 0,
            locked INTEGER DEFAULT 0
        )
    ''')

    # Salva as alterações no banco de dados e fecha a conexão
    conn.commit()
    conn.close()

# Chama a função para criar a tabela
create_table()
