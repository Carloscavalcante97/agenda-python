def deletar_contato(agenda,index_contato):
    if index_contato < 1 or index_contato > len(agenda):
        print("Número do contato inválido.")
        return
    contato = agenda[index_contato - 1]
    agenda.remove(contato)
    print(f"Contato {contato['nome']} removido da agenda.")