def listar_agenda(agenda):
    if not agenda:
        print("Nenhum contato encontrado.")
        return

    print("\nContatos:")
    for i, contato in enumerate(agenda, start=1):
        status = "[✔️]" if contato["favorito"] else "[ ]"
        print(f"{i}. {contato['nome']} {status}")
        print(f"   Telefone: {contato['telefone']}")
        print(f"   Email: {contato['email']}")