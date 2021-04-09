from database import Database


db = Database()
Categorias = list()
Produtos = list()


def show_categories():
    categories = db.cursor.execute('SELECT * FROM categorias').fetchall()
    [print(data) for data in categories]
        

def show_products():
    produtos = db.cursor.execute('''
    SELECT * FROM produtos
    JOIN produto_categoria ON produtos.id = produto_categoria.produto_id
    JOIN categorias ON categoria_id = produto_categoria.categoria_id
    ''').fetchall()
    [print(data) for data in produtos]


def menu():
    print("""                                  
            |    Olist Shops - Menu            |
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
        db.cursor.execute(f"""
        INSERT INTO categorias
        VALUES (?,?,?)
        """, (None, input('Categoria: '), input('Descricao: ')))
        db.commit()
    elif opcao == "2":
        show_categories()
    elif opcao == "3":
        db.cursor.execute("""
            INSERT INTO produtos
            VALUES (?,?,?,?)
        """, (None, input('Nome: '), input('Descrição: '), input('Valor: ')))
        produto_id = db.cursor.execute('SELECT id FROM produtos WHERE ID = (SELECT MAX (id) FROM produtos)').fetchall()
        db.cursor.execute('''
            INSERT INTO produto_categoria
            VALUES (?,?)
        ''', (produto_id[0][0], int(input('Digite o Id da categoria: ')))
        )
        db.commit()
    elif opcao == '4':
        show_products()

        print("------------------------------------------------------------------------------")

    elif opcao == '0':
        db.close()
        break
    else:
        print("Opção Inválida!")
