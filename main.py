import os

from acessoCliente import *
from acessoOperador import *
from colorama import init
from termcolor import colored
from interfaces import *
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
        cliente = Cliente(nome.title(), cpf)
        novoCliente(cliente)
        os.system('clear')


    menuCliente(cliente)

#Começa aqui
mostrarApresentacao()

while True:
    mostrarMenuPrincipal()
    escolha_Login = int(input())
    
    os.system('clear')

    if escolha_Login == 0:
        loginOperador()
    elif escolha_Login == 1:
        loginCliente()
    elif escolha_Login == 2:
        break



