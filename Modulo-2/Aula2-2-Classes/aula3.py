import uuid

class GeradorDeId:

    @staticmethod
    def gerar_id():
        return str(uuid.uuid4())

print(GeradorDeId().gerar_id())
print(GeradorDeId.gerar_id())

# o staticmethod não conhece nada sobre a classe, não pode acessar nenhum valor

class MinhaClasse:

    def __init__(self,nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @staticmethod
    def metodo_estatico():
        # ele não tem acesso aos atributos 
        # Não vai achar o valor de self.nome 
        print("Eu sou um metodo estático")