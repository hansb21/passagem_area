import os
import time
from acessoCliente import *
from acessoOperador import *
from colorama import init
from termcolor import colored

from reservas import *
from Cliente import *


def mostrarApresentacao():
    os.system('clear')

    print('*' * 51)
    print(colored('Bem vindo ao sistema de passagens aéreas Sputnik.', 'blue'))
    print('*' * 51)
    input()

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
        cliente = Cliente(nome.title(), cpf)
        novoCliente(cliente)
        os.system('clear')


    menuCliente(cliente)
def mostrarMenuPrincipal():
    os.system('clear')

    print(colored('**************************', 'green'))
    print(colored('0 - Operador              ', 'green'))
    print(colored('1 - Cliente               ', 'green'))
    print(colored('2 - Sair                  ', 'green'))
    print()
    print(colored('Como você deseja acessar: ', 'green'), end = '')
def escolhaMenu(n):
    if n == 0:
        os.system('clear')

        print('*' * 51)
        print(' ')
        print(colored('0 - Operador', 'red'))
        print(colored('1 - Cliente', 'green'))
        print(colored('2 - Sair','green'))            
        print(' ')
        time.sleep(1)
        loginOperador()
        
    elif n == 1:
        os.system('clear')
        print('*' * 51)
        print(' ')
        print(colored('0 - Operador', 'green'))
        print(colored('1 - Cliente', 'red'))
        print(colored('2 - Sair','green'))    
        print(' ')
        time.sleep(1)
        loginCliente()
        

        
