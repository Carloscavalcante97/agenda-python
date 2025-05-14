def adicionar_contato(agenda):
    nome= input("Digite o nome do novo contato: ")
    telefone= input("Digite o telefone do novo contato: ")
    email= input("Digite o email do novo contato: ")
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