# Crie uma classe de CadastroPessoa
# Crie uma classe de Cliente que herde da classe CadastroPessoa
# a classe CadastroPessoa deve conter um metodo que informa se a pessoa cadastrada é um cliente Vip ou não
#Exemplo de saída:
"""

cliente.tipo_de_cliente()
cliente_vip.tipo_de_cliente()

Junior é um cliente normal
Ana é um cliente Vip

"""

class CadastroPessoa:
    def __init__(self,nome, idade, vip=False):
        self.vip = vip
        self.nome = nome
        self.idade = idade

    def tipo_de_cliente(self):
        if self.vip:
            print(f"{self.nome} é um cliente Vip")
            return
        print(f"{self.nome} é um cliente normal")


class Cliente(CadastroPessoa):
    pass


cliente = Cliente(nome="Junior", idade=15, vip=False)
cliente_vip = Cliente(nome="Ana", idade=25, vip=True)

cliente.tipo_de_cliente()
cliente_vip.tipo_de_cliente()
