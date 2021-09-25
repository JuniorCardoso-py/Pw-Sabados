# Na aula anterior vimos sobre classes e objetos
# Nessa sessão veremos como estruturar uma classe com "atributos" e "funções"

def falar():
    print("Estou")

class Pessoa:

    def falar(self):
        print("Estou falando")

# Dentro dessa classe temos a função "falar"
# Para chamarmos essa função fazemos da seguinte forma

#Pessoa().falar()

# Inicializador da classe

# Como nos metodos podemos passar argumentos para os parametros de uma função
# Em uma classe para passarmos argumentos podemos fazer da seguinte forma

#def falar_algo(assunto="Livros"):
#    print(f" estou falando sobre {assunto}")

#falar_algo("Python")


class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.dicionario = {}

    def apresentar(self):
        print(f"Meu nome é {self.nome} tenho {self.idade} anos de idade e {self.altura} de altura")
        teste = "teste"
        return teste

    def printar(self):
        print(self.teste)

pablo = Pessoa("Pablo", 17, 1.68)

pablo.apresentar()



# O argumento self (que também é uma convenção de nome) refere-se a própria classe
# Por isso para acessar atributos ou métodos que pertencem a propria classe devemos sempre chamar por self


