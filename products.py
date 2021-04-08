
class Products:
              
    def menu(self):
        menu = (''' 
            *** Cadastro de Produtos ***

            1 - Novo produto
            2 - Listar produtos
            3 - Sair do programa
            
            Digite a opção desejada para iniciar o cadastro :
           ''')
        while True:
            option_menu = input(menu)
            if option_menu == "1":
                print('Novo produto')
            elif option_menu == "2":
                print('Listar Produtos')
            elif option_menu == "3":
                print("Sair do programa")
                break
            else:
                print("Opção inválida")    
                pass
          

             
    def crete_products(self):
        products = []
        name = str(input("Digite o produto a ser cadastrado :"))
        description = str(input("Descreva o produto :"))
        value = float(input("Valor R$ :"))
        all_products = {'name': name, 'description': description, 'value': value}
        for product in products:
            products.append(all_products)
        print(all_products)
   
    
product = Products()
#product.menu()
product.crete_products()