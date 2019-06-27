import os
from interfaces import *
import reservas
from colorama import init
from termcolor import colored

def menuCliente(cliento):
    global cliente
    cliente = cliento

    while True:
        mostrarMenuCliente(cliente.nome)

        opcao = int(input())
        os.system('clear')

        if opcao == 0:
            menuCadastrarPassagem()
        elif opcao == 1:
            menuConsultarPassagem()
        elif opcao == 2:
            menuCancelarPassagem()
        elif opcao == 3:
            break


def menuCadastrarPassagem():
    mostrarVoos(reservas.voosRegistrados)
    print('Qual vôo você quer comprar? \n')
    opcao = input('Para voltar ao menu aperte v: ')
    os.system('clear')

    if opcao.lower() == 'v': 
        return
    else:
        opcao = int(opcao)

    reservas.voosRegistrados[opcao].reservarPassagem(cliente)

def menuConsultarPassagem():
    mostrarVoos(cliente.getVoosComprados())

    input()
    os.system('clear')

    return

def menuCancelarPassagem():
    voosCancelaveis = cliente.getVoosComprados()
    mostrarVoos(voosCancelaveis)

    opcao = int(input())
    os.system('clear')

    reservas.cancelarPassagem(voosCancelaveis[opcao])
    return

def mostrarVoos(lista):
    print('----------------------------')
    for num, voo in enumerate(lista):
        voo.mostrarInformacoes(num)
    print('----------------------------')
