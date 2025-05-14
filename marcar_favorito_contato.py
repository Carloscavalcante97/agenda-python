def marcar_favorito(agenda, index_contato):
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