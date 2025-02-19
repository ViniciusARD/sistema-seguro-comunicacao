# Funcionalidades do Sistema

O sistema foi desenvolvido com o objetivo de garantir uma comunicação segura entre os usuários. As principais funcionalidades incluem:

### 1️⃣ Cadastro de Usuário
- O sistema permite que os usuários se cadastrem informando um nome de usuário e uma senha.
- A senha é protegida utilizando o algoritmo **bcrypt**, com a adição de um sal aleatório, para garantir sua segurança antes de ser armazenada no banco de dados.

### 2️⃣ Login
- O usuário faz login informando seu nome de usuário e senha.
- A senha fornecida é comparada com o hash armazenado no banco.
- Se a senha for válida, um **Token JWT** é gerado, permitindo que o usuário tenha acesso ao sistema por um tempo limitado.

### 3️⃣ Enviar Mensagem
- Quando um usuário envia uma mensagem, ela é criptografada utilizando **AES (Advanced Encryption Standard)** no modo **CBC**.
- Um vetor de inicialização (IV) aleatório é gerado para garantir a segurança e integridade da mensagem.
- A mensagem criptografada é armazenada no banco de dados, garantindo que apenas o destinatário correto possa acessá-la.

### 4️⃣ Receber Mensagem
- Para acessar a mensagem, o destinatário usa sua chave privada RSA para **descriptografar** a chave AES.
- A chave AES, agora recuperada, permite que o destinatário **descriptografe** a mensagem e a leia de forma segura.

