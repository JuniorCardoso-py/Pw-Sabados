# Crie uma classe que possa cadastrar Produtos 
# fazendo o uso dos modelos getters e setters
# Essa classe deve conter validações dos valores recebidos
# não podendo envia letras por exemplo
# Deve ter um cabeçalho
# Deve poder cadastrar os valores com o metodo input
# Deve ter um menu de escolhas
# Por exemplo

# 1. Cadastrar
# 2. Ler Todos
# 3. Ler 1 especifico
# 4. Apagar 

"""
 -------Bem Vindo--------

# 1. Cadastrar
# 2. Ler Todos
# 3. Ler 1 especifico
# 4. Apagar 

Digite um numero: 1

--------Menu de Cadastro-------

digite um nome:
digite um valor:
digite um categoria:

"""


# Crie uma classe que possa cadastrar Produtos 
# fazendo o uso dos modelos getters e setters
# Essa classe deve conter validações dos valores recebidos
# não podendo envia letras por exemplo
# Deve ter um cabeçalho
# Deve poder cadastrar os valores com o metodo input
# Deve ter um menu de escolhas
# Por exemplo

# 1. Cadastrar
# 2. Ler Todos
# 3. Ler 1 especifico
# 4. Apagar 

"""
 -------Bem Vindo--------

# 1. Cadastrar
# 2. Ler Todos
# 3. Ler 1 especifico
# 4. Apagar 

Digite um numero: 1

--------Menu de Cadastro-------

digite um nome:
digite um valor:
digite um categoria:

"""

from time import sleep

class Menu:

    choice = 0

    def main_menu(self):
        print("-"*25,"Bem Vindo","-"*25)
        print()
        print("1. Cadastrar")
        print("2. Ler Todos")
        print("3. Ler 1 especifico")
        print("4. Apagar")
        print("5. Voltar ao menu")
        print()
        self.choice = input("Digite a opção desejada: ")
        self.validate_choice()
    
    def validate_choice(self):
        try:
            self.choice = int(self.choice)
            if self.choice <= 0 or self.choice > 5:
                print("Por Favor escolha uma opção do menu")
                sleep(2)
                self.main_menu()
        except:
            print("Por Favor escolha uma opção do menu")
            sleep(2)
            self.main_menu()
        while self.choice == 5:
            self.main_menu()

    def menu_cadastro(self):
        print("-"*25,"Menu de Cadastro","-"*25)
        print()
    
    def menu_de_listagem(self):
        print("-"*25,"Lista","-"*25)
        print()

    def menu_deletar(self):
        print("-"*25,"Menu de delete","-"*25)
        print()
    
    def continuar_no_sistema(self):
        print("Deseja continuar no sitema? ")
        print("1. Sim")
        print("2. Não")
        print()
        try:
            opcao = int(input("Digite a opção escolhida: "))
            return opcao
        except:
            print("Por Favor escolha uma opção do menu")
            self.continuar_no_sistema()


class Produtos(Menu):

    name = ''
    price = ''
    category = ''

    def get_price(self):
        return self.price
    
    def get_category(self):
        return self.category

    def get_name(self):
        return self.name

    def set_price(self, price):
        try:
            price = float(price)
            self.price = price
        except:
            raise ValueError("Digite somente numeros")
        
    
    def set_name(self, name):
        self.__validate_value(name)
        self.name = name

    def set_category(self, category):
        self.__validate_value(category)
        self.category = category
    
    def __validate_value(self, value):
        if  not isinstance(value, str):
            raise ValueError("Somente letras são aceitas")
    

class Register(Produtos):

    database = {}
    identificador = 0

    def __init__(self) -> None:
        self.callback()


    def callback(self):
        self.main_menu()
        self.cadastrar_produto() if self.choice == 1 else ""
        self.listar_todos() if self.choice == 2 else ""
        self.listar_por_id() if self.choice == 3 else ""
        self.apagar() if self.choice == 4 else ""


    def cadastrar_produto(self):
        self.set_name(input("Digite um nome: "))
        self.set_price(input("Digite um valor: "))
        self.set_category(input("Digite uma categoria: ")) 

        self.identificador += 1

        self.database.update(
            {self.identificador:
                {
                    "nome":self.get_name(),
                    "preço":self.get_price(),
                    "categoria":self.get_category(),
                }
            })
        print()
        self.callback() if self.continuar_no_sistema() == 1 else print("Obrigado volte sempre")
    
    def listar_todos(self):
        self.menu_de_listagem()
        for ident, valores in self.database.items():
            print(ident, valores)
        print()
        self.callback() if self.continuar_no_sistema() == 1 else print("Obrigado volte sempre")

    
    def listar_por_id(self):
        self.menu_de_listagem()
        identifier = int(input("Escolha um produto para listar: "))
        for data in self.database:
            if identifier == data:
                identifier = self.database[data]
                print(data, identifier)
                break
        print()
        self.callback() if self.continuar_no_sistema() == 1 else print("Obrigado volte sempre !!")

    def apagar(self):
        self.menu_deletar()
        identifier = int(input("Escolha um produto para deletar: "))
        print()
        for ident, value in self.database.items():
            if identifier == ident:
                print(f"Produto {ident, value} DELETADO!!! ")
                del self.database[ident]
                identifier = None
                break
        print()
        self.callback() if self.continuar_no_sistema() == 1 else print("Obrigado volte sempre")



cadastrar = Register()