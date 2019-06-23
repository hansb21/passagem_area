#Sistema de login inicial do programa

import os
import time
while True:

    print('*'*51)
    print('1 - Operador')
    print('2 - Cliente' )
    print('3 - Sair')
    escolha = int(input('Como você deseja acessar: '))
    
    if escolha == (1):
        while True:
            os.system('clear')
            print('Por favor faça seu login. ')
            User = input('Login: ')
            senha = input('Senha: ')
            if User == 'admin' and senha == 'tigresvoadores': #Isso pode ser mudado, só tava pensando em uma senha não comum.....
                print('Acesso permitido.')
                print('os.system(''alguma coisa a ser feita'')')
                time.sleep(1)
            else:
                print('Login ou senha invalidos, tente novamente.')
                time.sleep(1)
    if escolha == 2:
        os.system('compras_Cliente.py')
    if escolha == 3:
        break

