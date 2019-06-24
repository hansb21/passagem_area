import os

from acessoCliente import *
from acessoOperador import *

while True:
    a = input('operador, cliente')
    os.system('clear')

    if a == '0':
        menuOperador()
    elif a == '1':
        menuCliente()



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
