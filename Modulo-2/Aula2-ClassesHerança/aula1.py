# Agora que já conhecemos sobre classes e alguns dos seus comportamentos
# Vamos conhecer uma outra pratica muito usada a Herança

# Existem dois tipos de Herança
# - Herança Simples
# - Herança Multipla

# Para este curso abordaremos a Herança simples

# O que é Herança na programação?
#
# Herança como o proprio nome ja diz é herdar algo de sua classe Pai ou SuperClass
# O que uma classe pode herdar para outra pode ser absolutamente tudo

# podemos pensar que a classe Filha e a classe Pai são praticamente a mesma classe pois
# instanciando a classe filha temos as mesmas caracteristicas da classe Pai
# Exemplo:



    # Aqui temos a classe Animal que é a classe pai nesse exemplo:
    # Se quisermos uma classe Cachorro por exemplo teriamos que repetir o mesmo código na classe Cachorro
    # Pois um animal pode ter patas, calda e emitir um som


# Como fazemos a Herança?

# Para herdar devemos criar a classe filha e nesta classe ao final do nome abrimos dois parenteses ()
# e passamos para esse parenteses o nome da classe Pai
# Exemplo:
class Animal:
    def __init__(self, patas, calda, som):
        self.patas = patas
        self.calda = calda
        self.som = som

    def emitir_som(self):
        print(self.som)

class Cachorro(Animal):
    
    def nadar(self):
        print("Sou um cachorro estou nadando")

class Cobra(Animal):
    
    def subir_em_arvores(self):
        print("Sou uma cobra e estou subindo na arvore")


cachorro = Cachorro(patas=4, calda=True, som="Au au au")
cachorro.emitir_som()
cachorro.nadar()

cobra = Cobra(patas=0, calda=True, som="ZZZzzzzZZZzzzzZ")
cobra.emitir_som()
cobra.subir_em_arvores()
