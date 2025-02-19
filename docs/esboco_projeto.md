# Esboço do Projeto

## 🎯 Objetivo
Garantir a segurança na comunicação entre funcionários da empresa, protegendo mensagens sensíveis contra acessos não autorizados.

## 🛠️ Tecnologias Utilizadas
- ✅ **bcrypt** → Hashing seguro de senhas.  
- ✅ **PyJWT** → Autenticação via Tokens JWT.  
- ✅ **cryptography** → Implementação de AES (criptografia simétrica) e RSA (criptografia assimétrica).  

## 🔄 Fluxo Básico do Sistema
1️⃣ O usuário faz **cadastro**, e a senha é armazenada de forma segura com **bcrypt**.  
2️⃣ O usuário faz **login**, sendo autenticado via **JWT**.  
3️⃣ O usuário pode **enviar uma mensagem criptografada** com **AES**.  
4️⃣ Apenas o destinatário correto pode **descriptografar** a mensagem usando sua **chave RSA**.  

