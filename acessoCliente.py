import os

from Reservas import *

cliente = clientesRegistrados[0]

def menuCliente():
    print('Cliente')
    a = input('cadastrar, consultar, cancelar')

    if a == '0':
        menuCadastrarPassagem()
    elif a == '1':
        menuConsultarPassagem()
    elif a == '2':
        menuCancelarPassagem()

def menuCadastrarPassagem():
    os.system('clear')
    mostrarVoos(voosRegistrados)

    r = int(input('qual vôo você quer \n'))
    voosRegistrados[r].reservarPassagem(cliente)

    menuCliente()

def menuConsultarPassagem():
    os.system('clear')
    mostrarVoos(cliente.voosComprados)

    print(cliente.getVoosComprados())

    input()
    menuCliente()

def menuCancelarPassagem():
    os.system('clear')
    mostrarVoos(cliente.voosComprados)

    input()
    menuCliente

def mostrarVoos(lista):
    print('----------------------------')
    for num, voo in enumerate(lista):
        print(num, voo.numeroDeVoo)
    print('----------------------------')
