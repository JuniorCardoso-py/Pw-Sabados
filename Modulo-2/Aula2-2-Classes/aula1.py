

class Pessoa:
    fruta = "'Abacaxi' "
    
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.valida_idade()

    def apresentar(self):
        print(f"Gosto de comer {self.fruta}")
        print(f"Olá meu nome é {self.idade} e tenho {self.nome} anos")

    def valida_idade(self):
        if self.idade < 18:
            print("Sou menor de idade")
        else:
            print("Sou maior de idade")

print(Pessoa.fruta)
Pessoa.fruta = "acerola"
print(Pessoa.fruta)
Pessoa(idade=17, nome="Junior")
# pessoa = Pessoa(idade=17,nome="Junior")



