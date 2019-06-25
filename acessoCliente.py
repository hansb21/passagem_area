import os
from colorama import init
from termcolor import colored
import reservas

def menuCliente(cliento):
    global cliente
    cliente = cliento
    while True:
        print(colored('*'*51, 'green'))
        print(colored('Seja bem vindo ao sistema de compras de passangens Sputink 1, {}. ', 'red').format(cliente.nome))
        for i in ['0 - Cadastrar', '1 - Consultar', '2 - Cancelar', '3 - Sair']:
            print(colored(i, 'red'))
        opcao = int(input(colored('Como você deseja acessar?', 'red')))
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

    opcao = input('qual vôo você quer \n')
    os.system('clear')

    if opcao == 'v': 
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
