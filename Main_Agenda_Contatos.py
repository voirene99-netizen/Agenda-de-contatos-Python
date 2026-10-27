from Funcoes import *
import os
print("\nBem-Vindo(a) a sua Agenda de Contatos")
Nome_usuario = input("Digite seu nome: ")

# Carrega a lista salva no JSON ao iniciar o programa

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
        case 1: # Adicionar contato
            os.system('cls')
            nome_contato = input("Digite o nome do contato a ser salvo: ")
            numero_contato = input("Digite o número de contato com DDD: ")

            numero_formatado = formatar_numero(numero_contato)

            if numero_formatado is None:
                print("\n[Erro] Número de contato inválido! Digite o DDD + número (10 ou 11 dígitos).")
                input("\nPressione Enter para voltar ao Menu de contatos...")
                continue
            else:
                add_contatos(contatos, nome_contato, numero_formatado)

        case 2: # Editar contato
            os.system('cls')
            ver_contatos(contatos)
            if not contatos:
                print("\nNenhum contato para editar.")
                input("\nPressione Enter para voltar ao Menu...")
                continue

            try:
                indice_contato = int(input("\nDigite qual contato você deseja editar: "))
            except ValueError:
                print("\nDigite apenas números válidos!")
                input("\nPressione Enter para voltar ao Menu...")
                continue

            if 0 < indice_contato <= len(contatos):
                novo_nome = input("Digite o novo nome para o contato: ")
                atualizar_nome_contato(contatos, indice_contato, novo_nome)
            else:
                print("\nNúmero não presente na lista.")
                input("\nPressione Enter para voltar ao Menu...")

        case 3:
            os.system('cls')
            ver_contatos(contatos)
            try:
                indice_contato_deletado = int(input("\nDigite qual contato você deseja deletar: "))
                if indice_contato_deletado > len(contatos) or indice_contato_deletado <= 0:
                    continue
            except ValueError:
                print("\nDigite apenas número!")
                input("\nPressione Enter para voltar ao Menu...")
                continue
            else:
                deletar_contato(contatos, indice_contato_deletado)
            
        case 4: 
            os.system('cls')
            ver_contatos(contatos)
            try:
                indice_favorito = int(input("Digite o indice do contato a ser favoritado: "))
            except ValueError:
                os.system('cls')
                print("\nDigite apenas números válidos!")
                input("\nPressione Enter para voltar ao Menu...")
                continue
            else:
                contato_favorito(contatos, indice_favorito)

        case 0: 
            os.system('cls')
            print("Programa Finalizado")
            break

        case _: 
            print("Opção não presente no Menu")
            input("Pressione Enter para voltar ao menu...")
