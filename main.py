import os

from acessoCliente import *
from acessoOperador import *

from reservas import *
from Cliente import *

def loginOperador():
    user  = input('Usuário: ')
    senha = input('Senha: ')
    os.system('clear')

    if user == 'admin' and senha == 'admin':
        menuOperador()

def loginCliente():
    nome = input('Nome: ')
    cpf  = input('CPF: ')
    os.system('clear')

    cliente = acharCliente(nome, cpf)

    if not cliente:
        cliente = Cliente(nome, cpf)
        novoCliente(cliente)

        print('Seja bem vindo ', cliente.nome)
        input()
        os.system('clear')

    
    menuCliente(cliente)

while True:
    a = input('operador, cliente')
    os.system('clear')

    if a == '0':
        loginOperador()
    elif a == '1':
        loginCliente()


# while True:
#     escolha = int(input('Como você deseja acessar: '))
#
#     if escolha == (1):
#         while True:
#             os.system('clear')
#             print('Por favor faça seu login. ')
#             User = input('Usuário: ')
#             senha = input('Senha: ')
#             if User == '' and senha == '': #Isso pode ser mudado, só tava pensando em uma senha não comum.....
#                 print('Acesso permitido.')
#                 print('os.system(''alguma coisa a ser feita'')')
#                 break
#                 time.sleep(1)
#             else:
#                 print('Login ou senha invalidos, tente novamente.')
#                 time.sleep(1)
#     if escolha == 2:
#         os.system('python compras_Cliente.py')
#     if escolha == 3:
#         break
