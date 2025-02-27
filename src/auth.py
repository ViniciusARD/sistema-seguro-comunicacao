import sqlite3
import bcrypt
import os

# Definir o caminho correto dentro da pasta src
db_path = os.path.join('src', 'users.db')

# Função para registrar um novo usuário
def register_user(username, password):
    # Conectar ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Verificar se o nome de usuário já existe
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        print(f"Erro: O usuário '{username}' já existe.")
        conn.close()
        return

    # Gerar o SALT e o hash da senha
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Inserir o novo usuário na tabela
    cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
    conn.commit()
    print(f"Usuário '{username}' registrado com sucesso.")

    # Fechar a conexão
    conn.close()

# Função para obter todos os usuários do banco de dados
def get_users():
    # Conectar ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Consultar todos os usuários
    cursor.execute('SELECT id, username, password_hash FROM users')
    users = cursor.fetchall()

    # Fechar a conexão
    conn.close()
    
    return users
