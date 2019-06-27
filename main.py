import os
import time

from colorama import init
from termcolor import colored

from acessoCliente import *
from acessoOperador import *
from interfaces import *
from reservas import *
from Cliente import *

def loginOperador():
    os.system('clear')

    user  = input(colored('Usuário: ', 'green'))
    senha = input(colored('Senha:   ', 'green'))
    os.system('clear')

    if user == 'admin' and senha == 'admin':
        menuOperador()

def loginCliente():
    os.system('clear')

    nome = input(colored('Nome: ', 'green'))
    cpf  = input(colored('CPF:  ', 'green'))
    os.system('clear')

    cliente = acharCliente(nome, cpf)

    if not cliente:
        cliente = Cliente(nome.title(), cpf)
        novoCliente(cliente)
        os.system('clear')

    menuCliente(cliente)

#Começa aqui
mostrarApresentacao()
 
while True:
    mostrarMenuPrincipal('')
    escolhaLogin = int(input())
    mostrarMenuPrincipal(escolhaLogin)

    if escolhaLogin == 0:
        loginOperador()
    elif escolhaLogin == 1:
        loginCliente()
    elif escolhaLogin == 2:
        break