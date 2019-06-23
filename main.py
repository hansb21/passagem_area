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
        print(colored('[1] - Cadastrar', 'blue', 'on_white'), end = ' ')
        print(colored('[2] - Consultar', 'blue','on_white'), end = ' ')
        print(colored('[3] - Remover','blue', 'on_white'), end = ' ')
        print(colored('[4] - Sair', 'blue', 'on_white'))
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

    max = len(voosRegistrados) - 1

    mostrarVoos(voosRegistrados)

    print(colored(f'[0 - {max}] - escolher', 'blue', 'on_white'), end = ' ')
    print(colored('[v] - voltar', 'blue', 'on_white'))
    print('')
    resposta = input(colored('Escolha uma opção: ','green'))

    cadastrar(resposta)
    menuPrincipal()

def cadastrar(resposta):
    if resposta == 'v':
        menuPrincipal()
    elif 0 <= int(resposta) < len(voosRegistrados):
        vooEscolhido = voosRegistrados[int(resposta)]
        vooEscolhido.reservarPassagem(cliente)
    else:
        os.system('clear')
        input(colored('RESPOSTA INVÁLIDA\n tente novamente\n', 'red'))
        menuCadastrar()

def menuConsultar():
    os.system('clear')

    mostrarVoos(cliente.voosComprados)
    input(colored('pressione enter para voltar', 'blue', 'on_white'))

    menuPrincipal()

def menuRemover():
    os.system('clear')

    mostrarVoos(cliente.voosComprados)

    resposta = int(input('qual vôo você quer remover\n'))
    cancelarPassagem(resposta)

    menuPrincipal()

def cancelarPassagem(index):
    vooPassagemCancelada = cliente.voosComprados[index]
    cliente.removerVoo(vooPassagemCancelada)
    vooPassagemCancelada.removerPassageiro(cliente)

def mostrarVoos(lista):
    max = len(voosRegistrados) - 1

    if max >= 1:
        print('-'*30)
        for num, voo in enumerate(lista):
            voo.informacoesDeVoo(num)
        print('-'*30)
    else:
        print('Nenhum voo disponível')

menuPrincipal()
