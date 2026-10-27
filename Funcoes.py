import os
def add_contatos(contatos, Nome_contato, Numero_contato):
    os.system('cls')
    contato = {"Nome_contato": Nome_contato, "Numero": Numero_contato, "Contato Favorito": False}
    contatos.append(contato)
    print(f"Contato: {Nome_contato}, foi adicionado com sucesso!")
    input("\nPressione Enter para voltar ao Menu de contatos...")

def contato_favorito(contatos, indice_contato):
    os.system('cls')
    indice_ajustado = indice_contato - 1 
    if 0<= indice_ajustado < len(contatos):
        contatos[indice_ajustado]["Contato Favorito"] = not contatos[indice_ajustado]["Contato Favorito"]
        status_txt = "favoritado" if contatos[indice_ajustado]["Contato Favorito"] else "desfavoritado"
        print(f"O contato '{contatos[indice_ajustado]['Nome_contato']}' foi {status_txt} com sucesso!")
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

def atualizar_nome_contato(contatos, indice_contatos, novo_nome_contato):
    os.system('cls')
    indice_ajustado = indice_contatos - 1
    contatos[indice_ajustado]["Nome_contato"] = novo_nome_contato
    print(f"O {indice_contatos}º item da lista foi atualizado para: {novo_nome_contato}")
    input("\nPressione Enter para voltar ao Menu...")

def deletar_contato(contatos, indice_contato):
    os.system('cls')
    indice_contato = indice_contato - 1
    print("O contato escolhido foi removido")
    contatos.pop(indice_contato)
    input("\nPressione Enter para voltar ao Menu...")
    return