from flask import Flask, render_template, request, redirect, url_for, flash
from auth import register_user, validate_user, get_users, delete_user
import os

# Definir o caminho absoluto para a pasta templates dentro de src
templates_path = os.path.abspath(os.path.join('src', 'templates'))

app = Flask(__name__, template_folder=templates_path)
app.secret_key = 'your_secret_key'  # Defina uma chave secreta para sessões

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if validate_user(username, password):
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('admin'))
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')
    
    return render_template('login.html')

@app.route('/admin')
def admin():
    users = get_users()  # Função para pegar todos os usuários
    return render_template('admin.html', users=users)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user_route(user_id):
    delete_user(user_id)  # Função para deletar usuário
    return redirect(url_for('admin'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        register_user(username, password)
        return redirect(url_for('register'))  # Redireciona para a página de registro novamente
    
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
