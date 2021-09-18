# Para garantir o comportamento de uma denominada aplicação é muito importante que tenhamos testes sobre a nossa aplicação

# Nessa secção veremos sobre o uso de asserts com unittest para verificar
# a veracidade do comportamento da função

# para gerar um teste devemos utilizar a palavra reservada assert

# Exemplo:

assert 1 == 1
# assert 1 == "1"
# assert 1 == 0

# podemos utilizar as condicionais para validar os testes.
# Exemplos:

lista_frutas = ["laranja", "uva", "abacaxi", "melancia"]

assert "laranja" in lista_frutas
# assert "laranja" not in lista_frutas
# assert not True
# assert not False

assert "laranja" in lista_frutas and len(lista_frutas) > 3
