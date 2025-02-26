from auth import register_user, get_users

def main():
    while True:
        # Perguntar se o usuário deseja registrar ou listar usuários
        print("\nEscolha uma opção:")
        print("1 - Registrar um novo usuário")
        print("2 - Listar todos os usuários registrados")
        print("3 - Sair")
        escolha = input("Digite o número da opção: ")

        if escolha == "1":
            # Solicitar nome de usuário e senha
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")
            register_user(username, password)

        elif escolha == "2":
            # Listar todos os usuários registrados
            print("\nLista de usuários registrados:")
            users = get_users()
            for user in users:
                print(f"ID: {user[0]}, Nome de usuário: {user[1]}, Hash da senha: {user[2]}")

        elif escolha == "3":
            # Sair do programa
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()