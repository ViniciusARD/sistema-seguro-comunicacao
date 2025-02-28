import sqlite3
import bcrypt
import os
from flask import flash

# Definir o caminho correto dentro da pasta src
db_path = os.path.join('src', 'users.db')

## Função para registrar um novo usuário
def register_user(username, password):
    # Conectar ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Verificar se o nome de usuário já existe
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        flash(f"Erro: O usuário '{username}' já existe.", 'danger')  # Usando flash para enviar a mensagem
        conn.close()
        return  # Retornar sem fazer a inserção

    # Gerar o SALT e o hash da senha
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Inserir o novo usuário na tabela
    cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
    conn.commit()
    flash(f"Usuário '{username}' registrado com sucesso.", 'success')  # Usando flash para enviar sucesso

    # Fechar a conexão
    conn.close()

# Função para validar o login do usuário
def validate_user(username, password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    if user:
        # Verificar se a senha corresponde ao hash armazenado
        stored_password_hash = user[2]  # O hash da senha
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
            conn.close()
            return True
    
    conn.close()
    return False


