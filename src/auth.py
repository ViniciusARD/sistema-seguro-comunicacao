import sqlite3
import bcrypt
import os
from flask import flash

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
        # Verificar se a conta está bloqueada
        if user[4] == 1:  # O campo "locked" está na posição 4
            flash('Conta bloqueada devido a múltiplas tentativas falhas.', 'danger')
            conn.close()
            return False
        
        # Verificar se a senha corresponde ao hash armazenado
        stored_password_hash = user[2]  # O hash da senha
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
            # Resetar tentativas falhas após login bem-sucedido
            cursor.execute('UPDATE users SET failed_attempts = 0 WHERE username = ?', (username,))
            conn.commit()
            conn.close()
            return True
        else:
            # Incrementar o número de tentativas falhas
            cursor.execute('UPDATE users SET failed_attempts = failed_attempts + 1 WHERE username = ?', (username,))
            conn.commit()

            # Verificar se o número de tentativas falhas atingiu o limite
            cursor.execute('SELECT failed_attempts FROM users WHERE username = ?', (username,))
            failed_attempts = cursor.fetchone()[0]

            if failed_attempts >= 5:
                # Bloquear a conta após 5 tentativas falhas
                cursor.execute('UPDATE users SET locked = 1 WHERE username = ?', (username,))
                conn.commit()
                flash('Conta bloqueada devido a múltiplas tentativas falhas.', 'danger')

            conn.close()
            return False
    
    conn.close()
    return False

