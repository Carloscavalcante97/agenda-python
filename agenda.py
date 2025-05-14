from adicionar_contato import adicionar_contato
from listar_agenda import listar_agenda
from atualizar_contato import atualizar_contato
from marcar_favorito_contato import marcar_favorito
from deletar_contato import deletar_contato
agenda = []

while True:
    print("\nMenu da Agenda")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Atualizar contato")
    print("4. Marcar contato como favorito")
    print("5. Deletar contato")
    print("6. Sair")

    try:
        entrada = input("Escolha uma opção: ").strip()
        opcao_menu = int(entrada)
        if opcao_menu == 1:
            nome_contato = input("Digite o nome do novo contato: ")
            telefone_contato = input("Digite o telefone do novo contato: ")
            email_contato = input("Digite o email do novo contato: ")
            adicionar_contato(agenda, nome_contato, telefone_contato, email_contato)
        elif opcao_menu == 2:
            listar_agenda(agenda)
        elif opcao_menu == 3:
            listar_agenda(agenda)
            index_contato = int(input("Digite o número do contato que deseja atualizar: "))
            atualizar_contato(agenda, index_contato)
        elif opcao_menu == 4:
            listar_agenda(agenda)
            index_contato = int(input("Digite o número do contato que deseja marcar como favorito: "))
            marcar_favorito(agenda, index_contato)
        elif opcao_menu == 5:
            listar_agenda(agenda)
            index_contato = int(input("Digite o número do contato que deseja deletar: "))
            deletar_contato(agenda, index_contato)
        elif opcao_menu == 6:
            print("Saindo do programa...")
            break
    except ValueError:
        print("Opção inválida. Por favor, escolha um número de 1 a 6.")
