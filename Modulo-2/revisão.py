nome = "Bob"

# print(nome) 

def dizer_nome(nome):
    print(nome)

# dizer_nome(nome)

class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade

    def dizer_nome(self, nome):
        print(self.__nome, nome)

    #Getter
    @property
    def nome(self):
        return self.__nome

    #Setter
    @nome.setter
    def nome(self, valor: str):
        self.__nome = valor

    @property
    def idade(self):
        return self.__idade

pessoa = Pessoa("Bob", 27)
print(pessoa.nome)
print(pessoa.idade)

# print(f"Ola meu nome é {pessoa.nome} e tenho {pessoa.idade} anos de idade \n")
# print("Teste")

# pessoa.dizer_nome("Marley")


class Usuario(Pessoa):
    pass

usuario = Usuario("Henrique", 23)

usuario.dizer_nome("& Renner")


pessoa = Pessoa(nome, 25)

assert 1 == 1
assert pessoa.nome == "Bob"
assert pessoa.idade == 25

assert pessoa.nome == "Bob" or pessoa.idade == "25"
assert pessoa.nome == "Bob" and pessoa.idade == 25

assert pessoa.idade != 20

import unittest
from unittest.case import TestCase

class TestPessoa(TestCase):

    def test_valores_iguas(self):
        self.assertEqual(1 , 1)


    def test_atributos_da_classe(self):
        # Preparação
        nome = "Dieter"
        idade = 27

        # Ação
        pessoa = Pessoa(nome, idade)
        
        #Asserção
        self.assertEqual(pessoa.idade, idade)
        self.assertEqual(pessoa.nome, nome)


if __name__ == "__main__":
    unittest.main()