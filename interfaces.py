from termcolor import colored
import os

def mostrarApresentacao():
    os.system('clear')

    print('*' * 51)
    print(colored('Bem vindo ao sistema de passagens aéreas Sputnik.', 'blue'))
    print('*' * 51)
    input()

def mostrarMenuPrincipal():
    os.system('clear')

    print(colored('**************************', 'green'))
    print(colored('0 - Operador              ', 'green'))
    print(colored('1 - Cliente               ', 'green'))
    print(colored('2 - Sair                  ', 'green'))
    print()
    print(colored('Como você deseja acessar: ', 'green'), end = '')
