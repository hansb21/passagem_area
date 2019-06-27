import os
import time
from acessoCliente import *
from acessoOperador import *
from colorama import init
from termcolor import colored
from interfaces import *
from reservas import *
from Cliente import *



#Começa aqui
mostrarApresentacao()

while True:
    mostrarMenuPrincipal()
    escolha_Login = int(input())
    if escolha_Login == 2:
        break
    else:
        escolhaMenu(escolha_Login)
    



