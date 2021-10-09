import unittest
from unittest import TestCase

class Pessoa:

    def __init__(self, nome, idade, email) -> None:
        self.nome = nome
        self.idade = idade
        self.email = email
        self.base_de_dados = []

    def cadastrar(self):
        self.base_de_dados.append(
            [self.nome, self.idade, self.email]
            )

class TestPessoa(TestCase):

    def setUp(self) -> None:
        self.pessoa = Pessoa("Wanderlei", 22, "wanderleiFeraDoPython@email.com")

    def test_criando_pessoa(self):
        
        self.assertIsInstance(self.pessoa, Pessoa)

    def test_atributos_da_classe_pessoa(self):

        self.assertIsInstance(self.pessoa.nome, str)
        self.assertIsInstance(self.pessoa.idade, int)
        self.assertIsInstance(self.pessoa.email, str)

    def test_metodo_cadastrar(self):

        self.pessoa.cadastrar()

        self.assertEqual(len(self.pessoa.base_de_dados), 1)


if __name__ == "__main__":
    unittest.main()

