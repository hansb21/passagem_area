import os
import time

from colorama import init
from termcolor import colored
from reservas import *

def mostrarApresentacao():
    os.system('clear')
    
    print(colored('       BEM VINDO AO SISTEMA DE PASSAGENS AÉREAS        ', 'red'))    

    print('*' * 55)
    print(colored('****** ****** **  ** ****** **   **  ** ******  **   **', 'blue'))
    print(colored('**     **  ** **  **   **   ** * **  ** **      ** **  ', 'blue'))
    print(colored('****** ****** **  **   **   **  ***  ** **      ****   ', 'blue'))
    print(colored('    ** **     **  **   **   **   **  ** **      ** **  ', 'blue'))
    print(colored('****** **     ******   **   **   **  ** ******  **   **', 'blue'))
    print('*' * 55)

    input()

def mostrarMenuPrincipal(n):
    os.system('clear')

    corOperador, corCliente = 'green', 'green'

    if n == 0:
        corOperador = 'red'
    elif n == 1:
        corCliente  = 'red'

    print(colored('**************************', 'green'))
    print(colored('0 - Operador              ',  corOperador))
    print(colored('1 - Cliente               ',  corCliente))
    print(colored('2 - Sair                  ', 'green'))
    print()
    print(colored('Como você deseja acessar: ', 'green'), end = '')
    print()
    time.sleep(0.5)

def mostrarMenuCliente(nome):
    os.system('clear')

    print(colored('MENU CLIENTE: {}          ', 'green').format(nome))
    print(colored('**************************', 'red'  ))
    print(colored('0 - Comprar Passagem      ', 'green'))
    print(colored('1 - Consultar Compras     ', 'green'))
    print(colored('2 - Cancelar Compra       ', 'green'))
    print(colored('3 - Voltar                ', 'green'))
    print()
    print(colored('Como você deseja acessar: ', 'green'), end = '')

def mostrarMenuOperador():
    os.system('clear')

    print(colored('MENU OPERADOR:            ', 'green'))
    print(colored('**************************', 'red'  ))
    print(colored('0 - Cadastrar Vôo         ', 'green'))
    print(colored('1 - Consultar Vôos        ', 'green'))
    print(colored('2 - Cancelar Vôos         ', 'green'))
    print(colored('3 - Voltar                ', 'green'))
    print()
    print(colored('Como você deseja acessar?: ', 'green'), end = '')

def mostrarTiposVoo():
    os.system('clear')

    print('0 - Transporte')
    print('1 - Comercial ')
    print('2 - Fretado   ')
    print()
    print('Escolha o tipo de vôo: ', end = '')

def mostrarVoos(lista):
    os.system('clear')
    
    print('*'*55)
    if lista == []:
        print('Não há voos para mostrar =(')

    for voo in lista:
        voo.mostrarInformacoes()
    print('*'*55)

def mostrarRestricoesAlimentares():
    print(colored('- Sem glúten       ', 'green'))
    print(colored('- Vegetariana      ', 'green'))
    print(colored('- Cardápio Infantil', 'green'))
    print()
    print(colored('Quantas das restrições acima você possui?: ', 'green'), end = '')