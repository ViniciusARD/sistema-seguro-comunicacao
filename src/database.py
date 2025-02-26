import sqlite3

def create_table():
    # Conectar ao banco de dados SQLite (será criado automaticamente)
    conn = sqlite3.connect('users.db')
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

# Chamar a função para garantir que a tabela seja criada
create_table()
