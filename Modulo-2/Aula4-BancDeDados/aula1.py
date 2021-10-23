# SGDB - Sistema Gerenciador de Banco de Dados

# Analogia
# Um SGDB podemos comparar com uma IDLE que utilizamos para formatar ou criar nossos codigos
# Como por exemplo o VsCode - Pycharm - Emac

# Um SGDB então serve para gerenciarmos um banco de dados podendo:
# 
#  - CRIAR TABELAS
#  - CRIAR BASE DE DADOS
#  - ALTERAR COLUNAS
#  - ALTERAR LINHAS INTEIRAS
#  - RESGATAR AS INFORMAÇÕES
#  - DELETAR
#  - INSERIR DADOS

# E muito mais finalidades 

# Exemplo de SGDBs
# MYSQL - POSTGRES - SQL SERVER - AURORA - ORACLE - SQLITE 


# BANCO DE DADOS

# Neste curso utilizaremos o MySQL para aprendizado de alguns conceitos e comandos

# Delete a base de dados que criamos
# e Crie uma base de dados nova 
# Com o mesmo nome `loja`
# Crie duas tabelas
# Uma tabela de produtos
# e uma tabela de Categoria

# Produtos deve conter id , nome, valor, id_categoria.
# Categoria deve conter id, nome

# Insira alguns dados nas duas tabelas
# Veja o resultado dos dados com o comando select 
# Atualize os dados com o comando update
# Delete alguns dados com o comando delete

# Comandos Necessarios 
# - SELECT * FROM nome_da_tabela ; Este comando mostrará todos os valores na tabela
# - UPDATE nome_da_tabela SET nome_do_campo=`valor_desejado` WHERE id=`id_desejado`; Este comando atualiza os campos
# - DELETE nome_da_tabela WHERE id=`id_desejado`; Este comando deleta uma linha com dados
# - INSERT INTO nome_da_tabela Values (`nome_dos_campos`, `separados_por_virgula`); Este comando insere dados na tabela
# - DROP DATABASE nome_da_base_de_dados; Este comando deleta a base de dados inteira
# - CREATE DATABASE nome_da_base_de_dados; Este comando cria uma base de dados

# - CREATE TABLE nome_da_tabela (
#    ---Dentro da tabela inserimos os dados com os seus respectivos `tipos` e configurações
#   
#    id int not null primary key,  --- Nessa parte criamos uma coluna com o nome de `id` ela sera do tipo 
#                                       inteiro(integer), not null = não pode ser vazia,
#                                       primary key = é o identificar unico desta tabela não pode se repetir, 
#                                       a primary key é utilizada para criarmos relações entre outras tabelas. 
#
#   nome varchar(60) not null, --- Nesta parte criamos uma coluna com o nome de `nome`, varchar significa que 
#                                  ela sera do tipo string varchar(60) significa que ela tera no maximo 60 caracteres

#   preco decimal(5,2) --- Nesta parte criamos uma coluna com o nome de `preco`, decimal(5,2) siginifica que podera ser
#                          um numero decimal de 5 casas sendo 2 após a virgula.
# );
# 
# - Outros comandos uteis são:
#   - USE nome_da_base_de_dados; Este comando seleciona a base de dados a ser usado no script do nosso SGBD.







