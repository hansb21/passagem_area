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
        print(colored('3 - Remover  ','blue', 'on_white'))
        print(colored('4 - Sair     ', 'blue', 'on_white'))
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

def menuCadastrar():
    os.system('clear')
    print('----------------------------')
    for num, voo in enumerate(voosRegistrados):
        print(num, '-', voo.numeroDeVoo)
        print(voo.passageiros)
    print('----------------------------')

    resposta = int(input('qual vôo você quer \n'))
    vooEscolhido = voosRegistrados[resposta]

    vooEscolhido.reservarPassagem(cliente)
    menuPrincipal()

def menuConsultar():
    os.system('clear')
    print('----------------------------')
    for num, voo in enumerate(cliente.voosComprados):
        print(num, '-', voo.numeroDeVoo)
    print('----------------------------')
    input()
    menuPrincipal()

def menuRemover():
    os.system('clear')
    print('----------------------------')
    for num, voo in enumerate(cliente.voosComprados):
        print(num, voo.numeroDeVoo)
    print('----------------------------')

    resposta = int(input('qual vôo você quer remover\n'))

    vooPassagemCancelada = cliente.voosComprados[resposta]

    cancelarPassagem(vooPassagemCancelada)
    menuPrincipal()

def cancelarPassagem(vooPassagemCancelada):
    cliente.removerVoo(vooPassagemCancelada)
    vooPassagemCancelada.removerPassageiro(cliente)

menuPrincipal()
