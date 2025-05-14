from listar_agenda import listar_agenda
def atualizar_contato(agenda):
    listar_agenda(agenda)
    index_contato = int(input("Digite o número do contato que deseja atualizar: "))
    if index_contato < 1 or index_contato > len(agenda):
        print("Número do contato inválido.")
        return
    novo_nome = input("Digite o novo nome do contato: ")
    novo_telefone = input("Digite o novo telefone do contato: ")
    novo_email = input("Digite o novo email do contato: ")
    agenda[index_contato - 1]["nome"] = novo_nome
    agenda[index_contato - 1]["telefone"] = novo_telefone
    agenda[index_contato - 1]["email"] = novo_email
    print(f"Contato {index_contato} atualizado para: {novo_nome}")
    