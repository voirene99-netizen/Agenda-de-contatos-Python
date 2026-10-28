import os
def remover_favorito(contatos):
    os.system('cls')
    ver_contatos(contatos)
    indice_contato = int(input("Digite o contato a ser desmarcado: "))
    os.system('cls')
    indice_ajustado = indice_contato - 1 
    contatos[indice_ajustado]["Contato Favorito"] = False
    print(f"O contato foi removido dos favoritos")
    input("\nPressione Enter para voltar ao Menu...")
    return

def add_contatos(contatos, Nome_contato, Numero_contato):
    os.system('cls')
    contato = {"Nome_contato": Nome_contato, "Numero": Numero_contato, "Contato Favorito": False}
    contatos.append(contato)
    print(f"Contato: {Nome_contato}, foi adicionado com sucesso!")
    input("\nPressione Enter para voltar ao Menu de contatos...")

def contato_favorito(contatos):
    os.system('cls')
    ver_contatos(contatos)
    try:
        indice_favorito = int(input("Digite o indice do contato a ser favoritado: "))
    except ValueError:
        os.system('cls')
        print("\nDigite apenas números válidos!")
        input("\nPressione Enter para voltar ao Menu...")

    os.system('cls')
    indice_favorito -= 1
    if 0<= indice_favorito < len(contatos):
        contatos[indice_favorito]["Contato Favorito"] = not contatos[indice_favorito]["Contato Favorito"]
        status_txt = "favoritado" if contatos[indice_favorito]["Contato Favorito"] else "desfavoritado"
        print(f"O contato '{contatos[indice_favorito]['Nome_contato']}' foi {status_txt} com sucesso!")
    else:
        print("\n[Erro] Número de contato inválido!")
    
    input("\nPressione Enter para voltar ao Menu...")
    return

def ver_contatos(contatos):
    for i, contato in enumerate(contatos, start=1):
        status = "★" if contato["Contato Favorito"] else " "
        nome_contato = contato["Nome_contato"]
        numero_contato = contato["Numero"]
        print(f"{i} - [{status}] {nome_contato} - {numero_contato}")

def formatar_numero(numero):
    digitos = "".join(filter(str.isdigit, numero))
    if len(digitos) == 11:  # Celular
        return f"({digitos[0:2]}) {digitos[2:7]}-{digitos[7:]}\n"
    elif len(digitos) == 10:  # Fixo
        return f"({digitos[0:2]}) {digitos[2:6]}-{digitos[6:]}\n"
    else:
        return None

def atualizar_nome_contato(contatos):
    os.system('cls')
    ver_contatos(contatos)
    if not contatos:
        print("\nNenhum contato para editar.")
        input("\nPressione Enter para voltar ao Menu...")  
    try:
        indice_contatos = int(input("\nDigite qual contato você deseja editar: "))
    except ValueError:
        print("\nDigite apenas números válidos!")
        input("\nPressione Enter para voltar ao Menu...")
        return

    if 0 < indice_contatos <= len(contatos):
        os.system('cls')
        novo_nome = input("Digite o novo nome para o contato: ")
    else:
        print("\nNúmero não presente na lista.")
        input("\nPressione Enter para voltar ao Menu...")

    os.system('cls')
    indice_ajustado = indice_contatos - 1
    contatos[indice_ajustado]["Nome_contato"] = novo_nome
    print(f"O {indice_contatos}º item da lista foi atualizado para: {novo_nome}")
    input("\nPressione Enter para voltar ao Menu...")

def deletar_contato(contatos):
    os.system('cls')
    ver_contatos(contatos)
    try:
        indice_contato = int(input("\nDigite qual contato você deseja deletar: "))  
        if indice_contato > len(contatos) or indice_contato <= 0:
            return
    except ValueError:
        print("\nDigite apenas número!")
        input("\nPressione Enter para voltar ao Menu...")

    os.system('cls')
    indice_contato = indice_contato - 1
    print("O contato escolhido foi removido")
    contatos.pop(indice_contato)
    input("\nPressione Enter para voltar ao Menu...")
    return

def forma_de_salvar(contatos):
    os.system('cls')
    nome_contato = input("Digite o nome do contato a ser salvo: ")
    print("""
=====================
1 - Salvar com número
2 - Salvar com gmail
=====================
""")
    
    op = int(input("Digite sua opção: "))
    if op is None:
        return
    match op:
        case 1:
            os.system('cls')
            numero_de_contato = input("Digite o número com o DDD do contato: ")
            if numero_de_contato is None:
                return
            formatar_numero(numero_de_contato)
            add_contatos(contatos, nome_contato, numero_de_contato)
            return
        case 2:
            os.system('cls')
            gmail_do_contato = input("Digite o gmail do contato: ")
            if gmail_do_contato is None:
                            return
            add_contatos(contatos, nome_contato, gmail_do_contato)
            return
