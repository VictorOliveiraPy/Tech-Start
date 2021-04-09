from database import Database as db

Categorias = list()
Produtos = list()


def show_categories():
    if DADOS:
        arquivo = open('dados.txt', 'r')
        for linha in arquivo:
            print(linha)
        arquivo.close()
    else:
        print("Categoria Vazia!")


def show_products():
    if products:
        arquivo = open('product.txt', 'r')
        for linha in arquivo:
            print(linha)
        arquivo.close()
    else:
        print("Produto Vazio!")


def save_categories():
    print(Categorias)
    db().cursor.execute(f"""
    INSERT INTO categorias
    VALUES ({Categorias[0]['name']},{Categorias[1]['descricao']})
    """)
    db().commit()



def save_products():
    with open('product.txt', 'a') as ex:
        for product in DADOS:
            ex.write(str(product) + '\n')


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


def criar_database():
    try:
        db().cursor.execute(
        '''
        CREATE TABLE produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        descricao VARCHAR(200) NOT NULL,
        valor FLOAT NOT NULL);'''
        )

        db().cursor.execute(
        '''
        CREATE TABLE produto_categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER,
            categoria_id INTEGER,
            FOREIGN KEY(produto_id) REFERENCES produtos(id),
            FOREIGN KEY(categoria_id) REFERENCES categorias(id)
        );
        '''
        )

        db().cursor.execute(
        '''
        CREATE TABLE categorias(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        descricao VARCHAR(100) NOT NULL
        );'''
        )
    except:
        pass


# EXECUÇÃO DO PROGRAMA

criar_database()

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        db().cursor.execute(f"""
        INSERT INTO categorias (nome, descricao)
        VALUES ({input('Categoria: ')},{input('Descricao: ')})
        """)
        # Categorias.append({"name": input('Categoria: ')})
        # Categorias.append({"descricao": input('Descricao: ')})
        # save_categories()
    elif opcao == "2":
        show_categories()
    elif opcao == "3":
        Produtos.append({"name": input('Produto: ')})
        Produtos.append({"description": input('Descricao: ')})
        Produtos.append({"value": input('Valor:')})
        save_products()
    elif opcao == '4':
        a = db().cursor.execute('SELECT * FROM categorias')
        print(a.fetchall())
        # show_products()

        print("------------------------------------------------------------------------------")

    elif opcao == '0':
        break
    else:
        print("Opção Inválida!")
