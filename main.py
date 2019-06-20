from Cliente import *
from Voos import *
from Reservas import *
from colorama import init
from termcolor import colored

import os

reserva = []

cliente = clientesRegistrados[0]

def menuPrincipal():
    os.system('clear')
    while True:
        print('*' * 51)
        print(colored('Bem vindo ao sistema de passagens aéreas Sputnik 1.', 'green'))
        print('*' * 51)
        print(' ')
        print(colored('1 - Cadastrar', 'blue', 'on_white'))
        print(colored('2 - Consultar', 'blue','on_white'))
        print(colored('3 - Remover','blue', 'on_white'))
        print(colored('4 - Sair', 'blue', 'on_white'))
        print(' ')
        resposta = int(input(colored('Escolha uma opção: ','green')))

        if resposta == 1:
            menuCadastrar()
            break
        elif resposta == 2:
            menuConsultar()
            break
        elif resposta == 3:
            menuRemover()
            break
        elif resposta == 4:
            print('Obrigado por utilizar nossos serviços.')
            break
        else:
            print('Tente novamente.')

# cadastro
def menuCadastrar():
    os.system('clear')
    print('----------------------------')
    for num, voo in enumerate(voosRegistrados):
        print(num, voo.numeroDeVoo)
    print('----------------------------')

    resposta = int(input('qual vôo você quer \n'))

    reservarPassagem(resposta)
    menuPrincipal()

def reservarPassagem(index):
    vooEscolhido = voosRegistrados[index]
    vooEscolhido.passageirosAtuais.append(cliente)
    cliente.voosComprados.append(vooEscolhido)

# consulta
def menuConsultar():
    os.system('clear')
    print('----------------------------')
    for num, voo in enumerate(cliente.voosComprados):
        print(num, voo.numeroDeVoo)
    print('----------------------------')
    input()
    menuPrincipal()

# remoção
def menuRemover():
    os.system('clear')
    print('----------------------------')
    for num, voo in enumerate(cliente.voosComprados):
        print(num, voo.numeroDeVoo)
    print('----------------------------')

    resposta = int(input('qual vôo você quer remover\n'))
    removerPassagem(resposta)
    menuPrincipal()

def removerPassagem(index):
    cliente.voosComprados.pop(index)
    # tirar esse cliente da lista desse vôo

menuPrincipal()
