import os

from Reservas import *

cliente = clientesRegistrados[0]

def menuCliente():
    print('Cliente')
    a = input('cadastrar, consultar, cancelar, voltar')
    os.system('clear')

    if a == '0':
        menuCadastrarPassagem()
    elif a == '1':
        menuConsultarPassagem()
    elif a == '2':
        menuCancelarPassagem()
    else:
        return

def menuCadastrarPassagem():
    mostrarVoos(voosRegistrados)

    r = input('qual vôo você quer \n')
    os.system('clear')

    if r == 'v': 
        return
    else:
        r = int(r)

    voosRegistrados[r].reservarPassagem(cliente)
    menuCliente()

def menuConsultarPassagem():
    mostrarVoos(cliente.voosComprados)

    print(cliente.getVoosComprados())

    input()
    os.system('clear')

    menuCliente()

def menuCancelarPassagem():
    mostrarVoos(cliente.voosComprados)

    input()
    os.system('clear')
    menuCliente()

def mostrarVoos(lista):
    print('----------------------------')
    for num, voo in enumerate(lista):
        voo.getInformacoes(num)
        # print(num, voo.numeroDeVoo)
    print('----------------------------')
