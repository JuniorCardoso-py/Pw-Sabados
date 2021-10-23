"""
_ protected
__ private
"""

_a = 'Protected'
__a = "Privado"

class Produto:

    def __init__(self,nome, valor) -> None:
        self.__nome = nome
        self.__valor = valor
        self.oi = "Oi"
    
    # Getter
    def ler_nome(self):
        return self.__nome

    #Getter
    def ler_valor(self):
        return self.__valor
    
    #Setter
    def configurar_nome(self, nome):
        self.__nome = nome
    
    #Setter
    def configurar_valor(self, valor):
        self.__valor = valor
    
    # 
    def __falar_algo(self):
        print("Falando Algo")

# produto = Produto("Refrigerante", 5.80)
# produto.oi = "Tchau"

# print(produto.oi)

# # Não Conseguimos alterar o valor da classe com attibutos privados
# produto.__nome = "Produto de limpeza"
# produto.__valor = 18.25
# produto.categoria = "Limpeza" 

# print(produto.__nome)
# print(produto.__valor)
# print(produto.categoria)
# print(produto.ler_nome())
# print(produto.ler_valor())

# produto.configurar_nome("Agua Tonica")
# print(produto.ler_nome())
# print(produto.__nome)
# produto.__falar_algo()

class Pessoa:

    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__idade = 24


pessoa = Pessoa("Botão")

# objeto._nome_da_classe__nome_do_atributo

print(pessoa._Pessoa__nome)
print(pessoa._Pessoa__idade)
