import sqlite3
import os

def create_table():
    # Garantir que a pasta src existe
    os.makedirs('src', exist_ok=True)

    # Caminho do banco de dados dentro da pasta src
    db_path = os.path.join('src', 'users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Apagar a tabela de usuários existente, se houver
    cursor.execute('DROP TABLE IF EXISTS users')

    # Criar a nova tabela de usuários com os campos adicionais
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password_hash TEXT,
            failed_attempts INTEGER DEFAULT 0,
            locked INTEGER DEFAULT 0
        )
    ''')

    # Commit e fechar a conexão
    conn.commit()
    conn.close()

# Criar a tabela (isso vai apagar a tabela antiga e criar uma nova)
create_table()
