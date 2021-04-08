DADOS = list()
products = {}


def show_categories():
    if DADOS:
        print(DADOS)
        print("------------------------------")
    else:
        print("Categoria Vazia!")


def show_products():
    if products:
        print(products)
        print("------------------------------")
    else:
        print("Produto Vazio!")


def save():
    with open('dados.txt', 'a') as a:
        for category in DADOS:
            a.write(str(category))


def menu():
    print("""                                  
            |    Olist Shops - Categoria       |
            |                                  |
            |                                  |
            | 1 - Nova Categoria               |
            | 2 - Lista Categoria              |
            | 3 - Criar Produto  
            | 4 - Lista Produtos               |
            | 0 - Sair do Programa             |
    """
          )


# EXECUÇÃO DO PROGRAMA

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        DADOS.append({"name": input('Categoria: ')})
        DADOS.append({"descricao": input('Descricao: ')})
        save()
    elif opcao == "2":
        show_categories()
    elif opcao == "3":
        products['name'] = str(input("Digite o produto a ser cadastrado :"))
        products['description'] = str(input("Descreva o produto :"))
        products['value'] = float(input("Valor R$ :"))
    elif opcao == '4':
        show_products()

        print("------------------------------------------------------------------------------")

    elif opcao == '0':
        break
    else:
        print("Opção Inválida!")
