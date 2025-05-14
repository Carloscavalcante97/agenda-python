from listar_agenda import listar_agenda
def marcar_favorito(agenda):
    listar_agenda(agenda)
    index_contato = int(input("Digite o número do contato que deseja marcar como favorito: "))
    if index_contato < 1 or index_contato > len(agenda):
        print("Número do contato inválido.")
        return
    contato = agenda[index_contato - 1]
    if contato["favorito"]:
        contato["favorito"] = False
        print(f"Contato {contato['nome']} removido dos favoritos.")
    else:
        contato["favorito"] = True
        print(f"Contato {contato['nome']} adicionado aos favoritos.")