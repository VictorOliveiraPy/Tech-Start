import products
from products import crete_products

Dados = {}


def show_categories():
    if Dados:
        print(Dados)
        print("------------------------------")
    else:
        print("Categoria Vazia!")


def show_products():
    if products:
        print(products)
        print("------------------------------")
    else:
        print("Produto Vazio!")


def menu():
    print("""                                  
            |    Olist Shops                   |
            |                                  |
            |                                  |
            | 1 - Nova Categoria               |
            | 2 - Lista Categoria              |
            | 3 - Criar Produto  
            | 4 - Lista Produtos
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
    elif opcao == "3":
        crete_products()
    elif opcao == '4':
        products.list_product()

        print("------------------------------------------------------------------------------")

    elif opcao == '0':
        break
    else:
        print("Opção Inválida!")
