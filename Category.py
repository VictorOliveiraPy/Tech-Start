
def menu():
    print("_______________________________________")
    print("|                                     |")
    print("|        Olist Shops - Categoria      |")
    print("|                                     |")
    print("|1 - Nova Categoria |")
    print("|2 - Lista Categoria      |")
    print("|0 - Sair do Programa                 |")
    print("|_____________________________________|")


# EXECUÇÃO DO PROGRAMA


while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        dados['name'] = str(input('Informe o nome da categoria :'))
        dados['descripino'] = str(input('Informe a descricao da categoria'))
    elif opcao == "2":
        print(dados)
        print("------------------------------------------------------------------------------")
    else:
        print("Opção Inválida!")
