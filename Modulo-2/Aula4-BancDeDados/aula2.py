from pymysql import cursors, connect
from time import sleep

conection = connect(host="localhost", user="root", password="12345678", database="loja", cursorclass=cursors.DictCursor)

cursor = conection.cursor()

# C   CREATE Criar 
# R   READ Ler
# U   UPDATE Atualizar
# D   DELETE Deletar


def read_all_products():
    sql = """
        SELECT * FROM produtos
    """
    cursor.execute(sql)
    products = cursor.fetchall()
    for dado in products:
        print(dado)

def insert_data(id, nome, preco):
    sql = f"""
        INSERT INTO produtos (id, nome, preco) VALUES ('{id}', '{nome}', '{preco}')
    """
    cursor.execute(sql)
    conection.commit()

def update_table(nome,preco, id):
    sql = f"""
        UPDATE produtos SET nome ='{nome}', preco='{preco}' WHERE id='{id}' 
    """
    cursor.execute(sql)
    conection.commit()

def delete_data(id):
    sql = f"""
        DELETE FROM produtos WHERE id='{id}'
    """
    cursor.execute(sql)
    conection.commit()


# read_all_products()
# insert_data(1,"Guaraná",5.50)
# update_table("Coquinha", 4.99, 1)
delete_data(1)
read_all_products()

("Banana", "Maçã") # Tupla
["Banana", "Maçã"] # Lista
{"banana":"Banana", "maca":"Maçã"} # Dicionario