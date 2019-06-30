import os
import time

from colorama import init
from termcolor import colored
from reservas import *

def mostrarApresentacao():
    os.system('clear')
    
    print(colored('       BEM VINDO AO SISTEMA DE PASSAGENS AÉREAS        ', 'yellow'))    

    print('*' * 55)
    print(colored('****** ****** **  ** ****** **   **  ** ******  **   **', 'red'))
    print(colored('**     **  ** **  **   **   ** * **  ** **      ** **  ', 'red'))
    print(colored('****** ****** **  **   **   **  ***  ** **      ****   ', 'red'))
    print(colored('    ** **     **  **   **   **   **  ** **      ** **  ', 'red'))
    print(colored('****** **     ******   **   **   **  ** ******  **   **', 'red'))
    print('*' * 55)

    input()

def mostrarMenuPrincipal(n):
    os.system('clear')

    corOperador, corCliente = 'red', 'red'

    if n == 0:
        corOperador = 'white'
    elif n == 1:
        corCliente  = 'white' 

    print(colored('**************************', 'yellow'))
    print(colored('0 - Operador              ',  corOperador))
    print(colored('1 - Cliente               ',  corCliente))
    print(colored('2 - Sair                  ', 'red'))
    print()
    print(colored('Como você deseja acessar: ', 'red'), end = '')
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

    print(colored('MENU OPERADOR:            ', 'blue'))
    print(colored('**************************', 'magenta'))
    print(colored('0 - Cadastrar Vôo         ', 'blue'))
    print(colored('1 - Consultar Vôos        ', 'blue'))
    print(colored('2 - Cancelar Vôos         ', 'blue'))
    print(colored('3 - Voltar                ', 'blue'))
    print()
    print(colored('Como você deseja acessar?: ', 'blue'), end = '')

def mostrarTiposVoo():
    os.system('clear')
    for i in ['0 - Transporte', '1 - Comercial', '2 - Fretado']:
        print(colored(i, 'blue'))
    print()
    print(colored('Escolha o tipo de vôo: ', 'blue'), end = '')

def mostrarVoos(lista):
    os.system('clear')
    
    print(colored('*'*55, 'blue'))
    if lista == []:
        print(colored('Não há voos para mostrar =(', 'red'))

    for voo in lista:
        voo.mostrarInformacoes()
    print(colored('*'*55, 'blue'))

def mostrarRestricoesAlimentares():
    print(colored('- Sem glúten       ', 'green'))
    print(colored('- Vegetariana      ', 'green'))
    print(colored('- Cardápio Infantil', 'green'))
    print()
    print(colored('Quantas das restrições acima você possui?: ', 'green'), end = '')
    