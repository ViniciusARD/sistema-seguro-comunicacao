# Proposta de Implementação

## 📌 Visão Geral
O sistema garantirá a segurança das credenciais e das mensagens trocadas entre os usuários, utilizando criptografia moderna e autenticação segura.

## 🛠️ Tecnologias Utilizadas e Aplicações
- **bcrypt** → Hashing seguro de senhas no cadastro e login.  
- **PyJWT** → Geração e verificação de Tokens JWT para autenticação.  
- **AES (CBC - Modo de Encadeamento de Blocos)** → Criptografia das mensagens trocadas entre os usuários.  
- **RSA** → Proteção da chave AES, permitindo que apenas o destinatário correto possa descriptografá-la.  

## 🔄 Etapas de Implementação

1️⃣ **Cadastro de Usuário**  
   - O usuário cadastra uma senha.  
   - A senha é **hasheada com bcrypt** antes de ser armazenada.  

2️⃣ **Login e Autenticação**  
   - O usuário insere suas credenciais.  
   - O sistema verifica a senha comparando com o hash armazenado.  
   - Se for válida, um **Token JWT** é gerado para autenticação.  

3️⃣ **Criptografia de Mensagens**  
   - A mensagem é **criptografada com AES (modo CBC)** antes de ser enviada.  
   - Uma **chave de inicialização (IV)** única é gerada para cada mensagem.  

4️⃣ **Proteção da Chave AES**  
   - A **chave AES é criptografada com RSA** antes de ser armazenada.  
   - Apenas o destinatário pode descriptografá-la usando sua **chave privada RSA**.  

## 🔒 Armazenamento Seguro de Dados
- As senhas são armazenadas apenas como **hashes bcrypt**.  
- Os Tokens JWT terão um **tempo de expiração curto** para reduzir riscos.  
- As mensagens criptografadas **não podem ser lidas sem a chave RSA correta**.  

---

Este plano garante um sistema seguro, protegendo credenciais e garantindo privacidade na comunicação. 🚀  

