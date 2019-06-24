#Sistema de login inicial do programa
from Cliente import *
import os
import time
from colorama import init
from termcolor import colored
clientes_aeroporto = Clientes()

while True:


    print(colored('*'*51, 'green'))
    print(colored('1 - Operador.', 'green'))
    print(colored('2 - Cliente.', 'green' ))
    print(colored('3 - Cadastrar novo cliente.', 'green'))
    print(colored('4 - Sair.', 'green'))
    print(' ')

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
                break
                time.sleep(1)
            else:
                print('Login ou senha invalidos, tente novamente.')
                time.sleep(1)
    if escolha == 2:
        login = input('Entre seu pin de login: ')
        try:
            if clientes_aeroporto.__pins[login] == True:
                os.system('python compras_Cliente.py')
        except:
            KeyError

    if escolha == 3:
        nome = input('Digite seu nome:  ')
        cpf = input('cpf:  ')
        try:
            cpf = int(cpf)
        except:
            TypeError
        clientes_aeroporto.adicionar_Cliente(nome, cpf)
            
    if escolha == 4:
            break

