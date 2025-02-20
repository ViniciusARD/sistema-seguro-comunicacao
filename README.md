# Sistema Seguro de Comunicação

## Descrição do Projeto

Este projeto visa implementar um sistema seguro de comunicação para uma empresa, garantindo a proteção das mensagens e credenciais dos funcionários, de forma que a comunicação interna seja privada e protegida contra acessos não autorizados. A solução utiliza tecnologias modernas de criptografia e autenticação, como **bcrypt**, **PyJWT**, **cryptography**, **AES** e **RSA**, para proteger tanto os dados armazenados quanto as mensagens transmitidas entre os usuários.

## Objetivo

Garantir a segurança na comunicação interna de uma empresa, implementando um sistema que proteja as credenciais dos usuários, autentique as sessões de forma segura e criptografe as mensagens trocadas entre os funcionários.

## Tecnologias Utilizadas

- **bcrypt**: Para **hashing seguro de senhas**. As senhas dos usuários nunca serão armazenadas em texto plano, mas sim como hashes seguros, utilizando o algoritmo bcrypt com sal aleatório.
- **PyJWT**: Para **autenticação via Tokens JWT**. O sistema gera um token JWT para autenticar os usuários, permitindo o acesso às funcionalidades protegidas do sistema de forma segura.
- **cryptography**: Para a **criptografia simétrica (AES)** das mensagens e a **criptografia assimétrica (RSA)** das chaves AES, garantindo que somente o destinatário correto possa acessar as mensagens criptografadas.

## Funcionalidades

### 1️⃣ **Cadastro de Usuário**
- O sistema permite que os usuários se cadastrem com um nome de usuário e uma senha.
- A senha fornecida é armazenada de forma segura utilizando o algoritmo **bcrypt** com sal aleatório.
- Nenhuma senha é armazenada em texto claro, garantindo a proteção contra vazamentos de dados.

### 2️⃣ **Autenticação de Usuário**
- O sistema permite que os usuários façam login informando seu nome de usuário e senha.
- A senha fornecida pelo usuário é comparada com o hash armazenado no banco de dados.
- Se a senha for válida, o sistema gera um **Token JWT** que contém informações do usuário e uma data de expiração, permitindo o acesso ao sistema por tempo limitado.

### 3️⃣ **Autorização com Token JWT**
- O sistema valida **Tokens JWT** para garantir que apenas usuários autenticados tenham acesso a funcionalidades protegidas.
- O token contém informações do usuário, como seu ID e a data de expiração do token, e é assinado digitalmente pelo servidor para garantir sua autenticidade.
- Tokens expirados ou inválidos são rejeitados automaticamente, e o acesso ao sistema é negado.

### 4️⃣ **Criptografia de Mensagens com AES**
- As mensagens enviadas entre os usuários são criptografadas utilizando **AES** (Advanced Encryption Standard), no modo **CBC (Cipher Block Chaining)**.
- Cada mensagem é criptografada com um **Vetor de Inicialização (IV)** único e aleatório, garantindo a segurança da comunicação.
- A mensagem criptografada é armazenada de forma segura, sendo acessível somente ao destinatário autorizado.

### 5️⃣ **Proteção da Chave AES com RSA**
- Cada usuário possui um par de chaves **RSA** (pública e privada).
- A chave **AES** utilizada para criptografar a mensagem é protegida com **RSA**: a chave AES é criptografada com a chave pública do destinatário antes de ser armazenada.
- O destinatário usa sua chave privada RSA para descriptografar a chave AES e, então, descriptografar a mensagem.
- Apenas o destinatário correto pode acessar a chave AES e a mensagem.

### 6️⃣ **Validação e Expiração de Tokens JWT**
- O sistema valida se o **Token JWT** não expirou antes de permitir o acesso a funcionalidades protegidas.
- Tokens expirados são rejeitados automaticamente, e os usuários precisam realizar novo login para obter um novo token de acesso.

## Requisitos Funcionais

### Funcionalidades Básicas:
- **Cadastro de Usuário**: O sistema deve permitir o cadastro de usuários com nome de usuário e senha, e deve armazenar a senha de forma segura com bcrypt.
- **Login e Geração de Token JWT**: O sistema deve validar o login do usuário e gerar um Token JWT se a senha for correta.
- **Autorização com JWT**: O sistema deve permitir o acesso às funcionalidades protegidas apenas a usuários com Tokens JWT válidos.
- **Criptografia de Mensagens**: As mensagens enviadas devem ser criptografadas com AES, garantindo a confidencialidade.
- **Proteção da Chave AES com RSA**: As chaves AES devem ser protegidas com RSA para que apenas o destinatário correto possa acessá-las.
- **Validação de Tokens**: O sistema deve validar a expiração do Token JWT para garantir que ele seja utilizado dentro do tempo válido.

## Requisitos Não Funcionais

### Segurança dos Dados:
- As senhas nunca devem ser armazenadas em texto claro.
- A chave AES nunca deve ser transmitida sem criptografia RSA.
- O sistema deve utilizar **algoritmos seguros** e atualizados para garantir a integridade dos dados.

### Desempenho e Eficiência:
- O sistema deve ser otimizado para garantir um bom desempenho durante o processo de autenticação e criptografia.
- A implementação deve balancear **segurança e tempo de execução** para garantir uma boa experiência do usuário.

### Facilidade de Manutenção:
- O código deve ser modularizado, documentado e fácil de manter.
- O sistema deve permitir a renovação de chaves RSA em caso de comprometimento.

### Portabilidade:
- O sistema deve ser compatível com **diferentes plataformas** que suportam Python.
- O código deve ser estruturado de forma modular para possibilitar futuras expansões.
