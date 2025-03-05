import sqlite3 
import bcrypt
import os
from flask import flash

# Caminho do banco de dados
db_path = os.path.join('src', 'users.db')

# Função para registrar um novo usuário
def register_user(username, password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Verifica se o nome de usuário já existe no banco
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        flash(f"Erro: O usuário '{username}' já existe.", 'danger')
        conn.close()
        return

    # Gera o salt e o hash da senha
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Insere o novo usuário na tabela
    cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
    conn.commit()
    flash(f"Usuário '{username}' registrado com sucesso.", 'success')

    conn.close()

# Função para obter todos os usuários, incluindo o hash da senha
def get_users():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Seleciona id, username, password_hash, failed_attempts e locked dos usuários
    cursor.execute('SELECT id, username, password_hash, failed_attempts, locked FROM users')
    users = cursor.fetchall()

    conn.close()
    return users

# Função para excluir um usuário
def delete_user(user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Deleta o usuário do banco de dados
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

    flash('Usuário excluído com sucesso!', 'success')
    conn.close()

# Função para validar o login
def validate_user(username, password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Verifica se o usuário existe
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    if user:
        # Verifica se a conta está bloqueada
        if user[4] == 1:  # Checa se o campo 'locked' está ativado
            flash('Conta bloqueada.', 'danger')
            conn.close()
            return False

        # Valida a senha com o hash armazenado
        stored_password_hash = user[2]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
            # Reseta o contador de falhas se o login for bem-sucedido
            cursor.execute('UPDATE users SET failed_attempts = 0 WHERE username = ?', (username,))
            conn.commit()
            conn.close()
            return True
        else:
            # Incrementa o contador de falhas
            cursor.execute('UPDATE users SET failed_attempts = failed_attempts + 1 WHERE username = ?', (username,))
            conn.commit()

            # Verifica se o número de falhas atingiu o limite
            cursor.execute('SELECT failed_attempts FROM users WHERE username = ?', (username,))
            failed_attempts = cursor.fetchone()[0]

            if failed_attempts >= 5:
                # Bloqueia a conta após 5 falhas
                cursor.execute('UPDATE users SET locked = 1 WHERE username = ?', (username,))
                conn.commit()
                flash('Conta bloqueada devido a múltiplas tentativas falhas.', 'danger')

            conn.close()
            return False
    
    conn.close()
    return False
