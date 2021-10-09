# Crie uma classe de Produtos
# Que tenha seus atributos privados __
# Utilizando o getter e setter para poder alterar seus valores
# Sem property 

class Produtos:
    
    def __init__(self, nome, valor) -> None:
        self.__nome= nome
        self.__valor= valor
    
    def get_nome(self):
        return self.__nome

    def get_valor(self):
        return self.__valor

    def configurar_nome(self,nome):
        self.__nome = nome
    
    def alterar_valor(self,valor):
        self.__valor = valor


produtos= Produtos(nome="Sabão em pó", valor=17.50)
# print(produtos.get_nome())
# print(produtos.get_valor())

# produtos.configurar_nome("Refrigerante")

# print(produtos.get_nome())

# produtos.alterar_valor(5.90)
# print(produtos.get_valor())

# Crie uma classe de Categorias
# Que tenha seus atributos privados __
# Utilizando o getter e setter para poder alterar seus valores
# Com property

class Categorias:
    
    def __init__(self, categoria) -> None:
        self.__categoria = categoria
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor

nome = Categorias("Bebidas")
print(nome.categoria)
nome.categoria = "Comida"
print(nome.categoria)