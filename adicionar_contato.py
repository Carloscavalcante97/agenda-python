def adicionar_contato(agenda,nome, telefone, email):
    contato ={
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    if (nome == "" or telefone == "" or email == ""):
        print("Contato não pode ser vazio.")
        return
    agenda.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")
    return