# Crie uma classe que contenha um classmethod 
# Que devera criar pelo ano de nascimento
# e validar se a idade é maior que 18

# Crie uma classe de produtos com classmethod
# Que valide se o valor do produto passado é um float
# A classe podera aceitar esse valor R$15.00
# Que devera ser transformado para um float

#Exemplo de aplicação
#
# nome = "CASCATA"
# nome.replace("A", "@")
#
#
# produto = Produto.cria_classe("RS15.00")
# print(produto.valor)
"""
>>>>> 15.00

"""

# Crie uma classe de cadastro de Pessoas usando o classmethod
# essa classe devera ter um atributo chamado banco_de_dados que será um dicionario vazio
# a classe deve Criar o cadastro de clientes com `nome idade id`
# o id deverá ser auto gerado se tiver um cliente com id 1 o proximo devera conter o id 2
#
# Exemplo
#
# CadastroCliente.criar_cadastro(nome, idade)
# Cadastro.listar_clientes()
"""
>>>> {clientes: {
    id:1, nome:"Fulano", idade:25,
    id:2, nome:"FulanoDeTal", idade:28,
    id:3, nome:"FooBar", idade:60
    }
}


"""