DADOS = list()
products = {}


def show_categories():
    if DADOS:
        arquivo = open('dados.txt', 'r')
        for linha in arquivo:
            print(linha)
        arquivo.close()
    else:
        print("Categoria Vazia!")


def show_products():
    if DADOS:
        arquivo = open('product.txt', 'r')
        for linha in arquivo:
            print(linha)
        arquivo.close()
    else:   
        print("Produto Vazio!")


def save():
    with open('dados.txt', 'a') as a:
        for category in DADOS:
            a.write(str(category) + '\n')


def save_products():
    with open('product.txt','a') as ex:
        for product in DADOS:
            ex.write(str(product) + '\n')            


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
        DADOS.append({"name": input('Produto: ')})
        DADOS.append({"description": input('Descricao: ')})
        DADOS.append({"value": input('Valor:')})
        save_products()
    elif opcao == '4':
        show_products()
    
        print("------------------------------------------------------------------------------")

    elif opcao == '0':
        break
    else:
        print("Opção Inválida!")
