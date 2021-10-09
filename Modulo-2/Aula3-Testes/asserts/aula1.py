import unittest
from unittest import TestCase

class Test(TestCase):

    def test_aprendendo_testar(self):
        assert 1 == 1

    def test_strigs(self):
        assert "1" == "1"
    
    def test_boleanos(self):
        assert True == True

    def test_booleano_dois(self):
        a = "Teste"
        assert bool(a)
    
    def test_varios_testes(self):
        a = "Teste"
        b = "Teste"
        c = ""
        assert a == b or a == c
        # or == palavra `OU`
        # a é igual a b ou a é igual a c?

    def test_com_and(self):
        a = "Teste"
        b = "Teste"
        c = ""
        assert a == b and a == c
    
    def test_valor_inteiro(self):
        assert isinstance(1, int)

if __name__ == "__main__":
    unittest.main()