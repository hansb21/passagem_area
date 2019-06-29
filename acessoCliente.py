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
    vooEscolhido = input('Digite o número do vôo que deseja comprar: ')
    os.system('clear')

    for voo in reservas.voosRegistrados:
        if voo.numeroDeVoo == vooEscolhido:
            voo.reservarPassagem(cliente)
            return
    else:
        input('Não foi possível cadastrar essa passagem')

def menuConsultarPassagem():
    mostrarVoos(cliente.getVoosComprados())
    input('Pressione qualquer tecla para voltar: ')

def menuCancelarPassagem():
    voosCancelaveis = cliente.getVoosComprados()
    mostrarVoos(voosCancelaveis)
    vooEscolhido = input('Digite o número do vôo que deseja cancelar: ')

    for voo in voosCancelaveis:
        if voo.numeroDeVoo == vooEscolhido:
            reservas.cancelarPassagem(voo)
    else:
        input('Não foi possível cancelar essa passagem')
