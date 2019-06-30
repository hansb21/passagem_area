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
    vooEscolhido = input(colored('Digite o número do vôo que deseja comprar: ', 'green'))
    os.system('clear')

    for voo in reservas.voosRegistrados:
        if voo.numeroDeVoo == vooEscolhido:
            voo.reservarPassagem(cliente)
            return
    else:
        input(colored('Não foi possível cadastrar essa passagem', 'green'))

def menuConsultarPassagem():
    mostrarVoos(cliente.getVoosComprados())
    input(colored('Pressione qualquer tecla para voltar: ', 'green'))

def menuCancelarPassagem():
    voosCancelaveis = cliente.getVoosComprados()
    mostrarVoos(voosCancelaveis)
    vooEscolhido = input(colored('Digite o número do vôo que deseja cancelar: ','green'))

    for voo in voosCancelaveis:
        if voo.numeroDeVoo == vooEscolhido:
            reservas.cancelarPassagem(voo)
            print(colored('Vôo cancelado com sucesso.', 'green'))
        else:
            input(colored('Não foi possível cancelar essa passagem', 'red'))
