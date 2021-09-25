# Crie uma classe de CadastroPessoa
# Crie uma classe de Cliente que herde da classe CadastroPessoa
# a classe CadastroPessoa deve conter um metodo que informa se a pessoa cadastrada é um 
# cliente Vip ou não
#Exemplo de saída:

class CadastroPessoa:
    def __init__(self, cliente_vip):
        self.vip = cliente_vip # <--- Pode ser um valor booleano False ou True

"""

cliente.tipo_de_cliente()
cliente_vip.tipo_de_cliente()

Junior é um cliente normal
Ana é um cliente Vip

"""
