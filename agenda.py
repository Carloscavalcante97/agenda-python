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
           
            adicionar_contato(agenda)
        elif opcao_menu == 2:
            listar_agenda(agenda)
        elif opcao_menu == 3:
            atualizar_contato(agenda)
        elif opcao_menu == 4:
            marcar_favorito(agenda)
        elif opcao_menu == 5:
            deletar_contato(agenda)
        elif opcao_menu == 6:
            print("Saindo do programa...")
            break
    except ValueError:
        print("Opção inválida. Por favor, escolha um número de 1 a 6.")
