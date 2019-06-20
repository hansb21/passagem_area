from Cliente import *
from Voos import *
from Reservas import *

import os

reserva = []

cliente = clientesRegistrados[0]

def menuPrincipal():
    os.system('clear')
    while True:
        print('*' * 51)
        print('Bem vindo ao sistema de passagens aéreas Sputnik 1.')
        print('*' * 51)
        print(' ')
        print('1 - Cadastrar')
        print('2 - Consultar')
        print('3 - Remover')
        print('4 - Sair')
        resposta = int(input('Escolha uma opção: '))

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
