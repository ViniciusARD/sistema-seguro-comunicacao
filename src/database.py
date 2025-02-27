import sqlite3
import os

def create_table():
    # Garantir que a pasta src existe
    os.makedirs('src', exist_ok=True)

    # Caminho do banco de dados dentro da pasta src
    db_path = os.path.join('src', 'users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Criar a tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password_hash TEXT
        )
    ''')

    # Commit e fechar a conexão
    conn.commit()
    conn.close()

# Criar a tabela
create_table()
