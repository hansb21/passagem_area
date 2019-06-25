import os

from acessoCliente import *
from acessoOperador import *
from colorama import init
from termcolor import colored
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
        os.system('clear')

    
    menuCliente(cliente)

while True:
    print(colored('*'*51, 'green'))
    for i in ['0 - Operador.', '1 - Cliente.', '2 - Sair.']:
        print(colored(i, 'green'))
    
    escolha_Login = int(input(colored('Como você deseja acessar: ', 'green')))
    os.system('clear')

    if escolha_Login == 0:
        loginOperador()
    elif escolha_Login == 1:
        loginCliente()
    elif escolha_Login == 2:
        break



