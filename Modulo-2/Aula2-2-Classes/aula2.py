"""
classmethod  - staticmethod - decorators
"""

class MinhaClasse:

    def __init__(self,nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def metodo_de_instancia(self):
        print(f"Eu sou uma classe {self}")
        print(f"Meu nome é {self.nome}")

    @classmethod
    def metodo_de_classe(cls,nome,idade):
        if idade < 18:
            raise Exception("Não pode menor de idade")
        return cls(nome,idade)

    @staticmethod
    def metodo_estatico():
        print("Eu sou um metodo estático")


minha_classe = MinhaClasse(nome="Vanderlei", idade=25)


outra_classe = MinhaClasse.metodo_de_classe("Junior",19)
print(outra_classe.idade)

# classmethod normalmente usado para criar classes apartir dele, 
# o classmethod conhece o que existe dentro da classe 
# podendo alterar os atributos da classe por exemplo os atributos 
# que existem dentro do  __init__








