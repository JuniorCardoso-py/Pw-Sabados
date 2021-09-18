# Crie uma classe que escreva em um arquivo
# Crie uma classe que crie um produto para registrar dentro do arquivo
# Criterios:
# Os Produtos devem conter:
#   - id(integer)
#   - nome(string)
#   - preço(float)

# Cadastre ao menos 5 produtos e faça com que sejam impressos no terminal
# Exemplo de saída

"""
{'id': 1, 'nome': 'coca-cola', 'preço': 5.79}

{'id': 2, 'nome': 'pepsi', 'preço': 5.79}

{'id': 3, 'nome': 'fanta', 'preço': 5.79}

{'id': 4, 'nome': 'guaraná', 'preço': 5.79}

{'id': 5, 'nome': 'Sprite', 'preço': 5.79}
"""

class Produto:

    def __init__(self):
        self.produtos = []

    def criar_produto(self, id, nome, preco):
        self.produtos.append({"id": id, "nome": nome, "preço": preco})


produto = Produto()
produto.criar_produto(1, "coca-cola", 5.79)
produto.criar_produto(1, "coca-cola", 5.79)
produto.criar_produto(1, "coca-cola", 5.79)
produto.criar_produto(1, "coca-cola", 5.79)


class Escritor:

    def escrever(self, dados_produto):
        with open("products.txt", "a") as file:
            for item in produto.produtos:
                file.write(str(item) + "\n")

    def ler_registros(self):
        with open("products.txt", "r") as file:
            for product in file.readlines():
                print(product)


molde = Escritor()
molde.ler_registros()
