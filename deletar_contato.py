from listar_agenda import listar_agenda
def deletar_contato(agenda):
    listar_agenda(agenda)
    index_contato = int(input("Digite o número do contato que deseja remover: "))
    if index_contato < 1 or index_contato > len(agenda):
        print("Número do contato inválido.")
        return
    contato = agenda[index_contato - 1]
    agenda.remove(contato)
    print(f"Contato {contato['nome']} removido da agenda.")