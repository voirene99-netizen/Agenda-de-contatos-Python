from Funcoes import *
import os
print("\nBem-Vindo(a) a sua Agenda de Contatos")
Nome_usuario = input("Digite seu nome: ")

contatos = []

while True:
    os.system('cls')
    print(f"Contatos: [{len(contatos)}] ")
    print("--------------------")
    if len(contatos) >= 1:
        ver_contatos(contatos)
    else:
        print(" Nenhum contato salvo ")
    print("--------------------\n")
    print("""
Agenda de Contatos
====================
1. Adicionar Contato
2. Editar Contato
3. Deletar Contato
4. Marcar contato como Favorito
5. Desmarcar como favorito
0. Sair
====================
    """)

    if len(contatos) == 0:
        print(f"{Nome_usuario}, você ainda não possui nenhum contato!")

    try:
        op = int(input("\nDigite sua opção: "))
    except ValueError:
        continue

    match op:
        case 1: 
            forma_de_salvar(contatos)
        case 2:
            atualizar_nome_contato(contatos)
        case 3:
            deletar_contato(contatos)
        case 4: 
            contato_favorito(contatos)
        case 5:
            remover_favorito(contatos)
        case 0: 
            os.system('cls')
            print("Programa Finalizado")
            break
        case _: 
            print("Opção não presente no Menu")
            input("Pressione Enter para voltar ao menu...")
