products = {}


def crete_products():
    products['name'] = str(input("Digite o produto a ser cadastrado :"))
    products['description'] = str(input("Descreva o produto :"))
    products['value'] = float(input("Valor R$ :"))


def list_product():
    for product in products:
        print(product['name'])
