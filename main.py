#Sistema de login inicial do programa

import os
import time
from colorama import init
from termcolor import colored
while True:

    print(colored('*'*51, 'green'))
    print(colored('1 - Operador', 'green'))
    print(colored('2 - Cliente', 'green' ))
    print(colored('3 - Sair', 'green'))
    print(' ')
    while True:
        escolha = int(input('Como você deseja acessar: '))

        if escolha == (1):
            while True:
                os.system('clear')
                print('Por favor faça seu login. ')
                User = input('Usuário: ')
                senha = input('Senha: ')
                if User == 'admin' and senha == 'tigresvoadores': #Isso pode ser mudado, só tava pensando em uma senha não comum.....
                    print('Acesso permitido.')
                    print('os.system(''alguma coisa a ser feita'')')
                    break
                    time.sleep(1)
                else:
                    print('Login ou senha invalidos, tente novamente.')
                    time.sleep(1)
        if escolha == 2:
            os.system('python compras_Cliente.py')
        if escolha == 3:
            break
