import os
import time

from colorama import init
from termcolor import colored

from acessoCliente import *
from acessoOperador import *
from reservas import *
from Cliente import *

def mostrarApresentacao():
    os.system('clear')

    print('*' * 51)
    print(colored('Bem vindo ao sistema de passagens aéreas Sputnik.', 'blue'))
    print('*' * 51)
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
    time.sleep(1)

def mostrarMenuCliente(nome):
    os.system('clear')

    print(colored('MENU CLIENTE: {}', 'green').format(nome))
    print(colored('**************************', 'red'))
    print(colored('0 - Comprar Passagem      ', 'green'))
    print(colored('1 - Consultar Compras     ', 'green'))
    print(colored('2 - Cancelar Compra       ', 'green'))
    print(colored('3 - Voltar                ', 'green'))
    print()
    print(colored('Como você deseja acessar: ', 'green'), end = '')
