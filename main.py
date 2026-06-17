from models.usuario import cadastrar_usuario, login
from models.vaga import cadastrar_vaga, listar_vagas
from models.candidatura import candidatar, minhas_candidaturas

usuario_logado = None

while True:

    print("\n===== SISTEMA DE VAGAS =====")
    print("1 - Cadastrar Usuário")
    print("2 - Login")
    print("3 - Cadastrar Vaga")
    print("4 - Listar Vagas")
    print("5 - Candidatar-se")
    print("6 - Ver Minhas Candidaturas")
    print("7 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # CADASTRO DE USUÁRIO
    if opcao == "1":

        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")

        cadastrar_usuario(nome, email, senha)

    # LOGIN
    elif opcao == "2":

        email = input("Email: ")
        senha = input("Senha: ")

        usuario = login(email, senha)

        if usuario:
            usuario_logado = usuario

            print("\nLogin realizado com sucesso!")
            print(f"Bem-vindo, {usuario[1]}!")

        else:
            print("\nEmail ou senha incorretos!")

    # CADASTRAR VAGA
    elif opcao == "3":

        titulo = input("Título da vaga: ")
        empresa = input("Empresa: ")
        descricao = input("Descrição da vaga: ")

        cadastrar_vaga(titulo, empresa, descricao)

    # LISTAR VAGAS
    elif opcao == "4":

        vagas = listar_vagas()

        print("\n===== VAGAS DISPONÍVEIS =====")

        if vagas:

            for vaga in vagas:

                print(f"""
ID: {vaga[0]}
Título: {vaga[1]}
Empresa: {vaga[2]}
Descrição: {vaga[3]}
-----------------------------
""")
        else:
            print("Nenhuma vaga cadastrada.")

    # CANDIDATAR-SE
    elif opcao == "5":

        if usuario_logado:

            vagas = listar_vagas()

            print("\n===== VAGAS DISPONÍVEIS =====")

            for vaga in vagas:
                print(f"{vaga[0]} - {vaga[1]}")

            vaga_id = int(input("\nDigite o ID da vaga: "))

            candidatar(usuario_logado[0], vaga_id)

        else:
            print("\nFaça login primeiro!")

    # VER CANDIDATURAS
    elif opcao == "6":

        if usuario_logado:

            vagas = minhas_candidaturas(usuario_logado[0])

            print("\n===== MINHAS CANDIDATURAS =====")

            if vagas:

                for vaga in vagas:
                    print(f"✓ {vaga[0]}")

            else:
                print("Você ainda não se candidatou para nenhuma vaga.")

        else:
            print("\nFaça login primeiro!")

    # SAIR
    elif opcao == "7":

        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida!")