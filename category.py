Dados = {}


def show_categories():
    if Dados:
        print(Dados)
        print("------------------------------")
    else:
        print("Categoria Vazia!")


def menu():
    print("""                                  
            |    Olist Shops - Categoria       |
            |                                  |
            |                                  |
            | 1 - Nova Categoria               |
            | 2 - Lista Categoria              |
            | 3 - Editar um Contato da Agenda  |
            | 0 - Sair do Programa             |
    """
          )


# EXECUÇÃO DO PROGRAMA

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        Dados['name'] = str(input('Categoria: '))
        Dados['description'] = str(input('Descrição: '))
    elif opcao == "2":
        show_categories()
        print("------------------------------------------------------------------------------")

    elif opcao == '0':
        break
    else:
        print("Opção Inválida!")
