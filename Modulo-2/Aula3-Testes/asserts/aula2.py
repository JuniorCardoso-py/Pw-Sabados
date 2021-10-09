# import unittest

# class TestModel(unittest.TestCase):

#     def test_alguma_coisa(self):
        
#         # assert 1 == 1
#         self.assertEqual(1,1)

#     def test_assert_false(self):
#         a = " "
#         a = a.strip()

#         # assert False
#         self.assertFalse(a)

#     def test_outro_teste(self):
#         self.assertIsInstance(1, int)


class Pessoa:

    def __init__(self,nome, idade, email) -> None:
        self.nome = self.valida_nome(nome)
        self.idade = self.valida_idade(idade)
        self.email = self.valida_email(email)

    def valida_idade(self, idade):
        if not isinstance(idade, int):
            raise ValueError()
        return idade

    def valida_nome(self, nome):
        if not isinstance(nome, str):
            raise ValueError()
        return nome

    def valida_email(self,email):
        if "@" not in email:
            raise ValueError()
        return email

import unittest
from unittest import TestCase


class TestPessoa(TestCase):

    def test_cria_pessoa(self):
        pessoa = Pessoa("Marley", 25, "email_da_pessoa@proway.com")

        self.assertIsInstance(pessoa, Pessoa)
    
    def test_pessoa_com_valor_correto_nos_atributos(self):

        pessoa = Pessoa(nome="Marley", idade=25, email="email_da_pessoa@proway.com")

        self.assertIsInstance(pessoa.nome, str)
        self.assertIsInstance(pessoa.idade, int)
        self.assertIsInstance(pessoa.email, str)

    def test_valores_esperados(self):
        # Preparação do teste
        nome = "Marley"
        idade = 25
        email = "email_da_pessoa@proway.com"

        # Ação ou Execução
        pessoa = Pessoa(nome,idade,email)

        # Asserção
        self.assertEqual(pessoa.nome, nome)
        self.assertEqual(pessoa.idade, idade)
        self.assertEqual(pessoa.email, email)



if __name__ == "__main__":
    unittest.main()