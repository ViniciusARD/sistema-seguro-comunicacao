from flask import Flask, render_template, request, redirect, url_for, flash, session
from auth import register_user, validate_user, get_users, delete_user
import os

# Definir o caminho absoluto para a pasta templates dentro de src
templates_path = os.path.abspath(os.path.join('src', 'templates'))

# Criação do aplicativo Flask
app = Flask(__name__, template_folder=templates_path)
app.secret_key = 'your_secret_key'  # Chave secreta para sessões

# Rota principal da página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para login (GET para exibir o formulário, POST para validar o login)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Valida o login utilizando a função do auth.py
        if validate_user(username, password):
            session['username'] = username  # Armazena o nome de usuário na sessão
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('admin'))  # Redireciona para o painel de administração
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')
    
    return render_template('login.html')

# Rota para o painel de administração (lista todos os usuários)
@app.route('/admin')
def admin():
    if 'username' not in session:  # Verifica se o usuário está autenticado
        flash('Por favor, faça login para acessar o painel de administração.', 'danger')
        return redirect(url_for('login'))  # Redireciona para a página de login
    
    users = get_users()  # Obtém todos os usuários com o hash da senha e informações adicionais
    return render_template('admin.html', users=users)

# Rota para excluir um usuário (com base no ID do usuário)
@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user_route(user_id):
    delete_user(user_id)  # Função para excluir o usuário
    return redirect(url_for('admin'))  # Redireciona de volta para o painel de administração

# Rota para registrar um novo usuário (GET para exibir o formulário, POST para registrar o usuário)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        register_user(username, password)  # Registra o novo usuário
        return redirect(url_for('register'))  # Redireciona para a página de registro novamente
    
    return render_template('register.html')

# Rodar o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
