import sqlite3
import bcrypt
import os
from flask import flash

db_path = os.path.join('src', 'users.db')

# Função para registrar um novo usuário
def register_user(username, password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        flash(f"Erro: O usuário '{username}' já existe.", 'danger')
        conn.close()
        return

    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

    cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
    conn.commit()
    flash(f"Usuário '{username}' registrado com sucesso.", 'success')

    conn.close()

# Função para obter todos os usuários
def get_users():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT id, username, failed_attempts, locked FROM users')
    users = cursor.fetchall()

    conn.close()
    return users

# Função para excluir um usuário
def delete_user(user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

    flash('Usuário excluído com sucesso!', 'success')
    conn.close()

# Função para validar o login
def validate_user(username, password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    if user:
        if user[4] == 1:  # Checar se a conta está bloqueada
            flash('Conta bloqueada.', 'danger')
            conn.close()
            return False

        stored_password_hash = user[2]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
            cursor.execute('UPDATE users SET failed_attempts = 0 WHERE username = ?', (username,))
            conn.commit()
            conn.close()
            return True
        else:
            cursor.execute('UPDATE users SET failed_attempts = failed_attempts + 1 WHERE username = ?', (username,))
            conn.commit()

            cursor.execute('SELECT failed_attempts FROM users WHERE username = ?', (username,))
            failed_attempts = cursor.fetchone()[0]

            if failed_attempts >= 5:
                cursor.execute('UPDATE users SET locked = 1 WHERE username = ?', (username,))
                conn.commit()
                flash('Conta bloqueada devido a múltiplas tentativas falhas.', 'danger')

            conn.close()
            return False
    
    conn.close()
    return False
