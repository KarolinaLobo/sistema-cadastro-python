def menu():
    print("\n=== Sistema de Cadastro ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("0 - Sair")

usuarios = []

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        usuarios.append({"nome": nome, "idade": idade})
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. {usuario['nome']} - {usuario['idade']} anos")

    elif opcao == "3":
        busca = input("Digite o nome para buscar: ")
        encontrado = False
        for usuario in usuarios:
            if usuario["nome"].lower() == busca.lower():
                print(f"Encontrado: {usuario['nome']} - {usuario['idade']} anos")
                encontrado = True
                break
        if not encontrado:
            print("Usuário não encontrado.")

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
