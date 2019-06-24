import Reservas
import os

from Voos import *

def menuOperador():
    print('Operador')
    a = input('cadastrar, consultar, cancelar, voltar')
    os.system('clear')

    if a == '0':
        menuCadastrarVoo()
    elif a == '1':
        menuConsultarVoo()
    elif a == '2':
        print('meucu')
        # menuCancelarVoo()
        
def menuCadastrarVoo():
    tipo = input('tipo')
    num = input('num')
    origem = input('origem')
    destino = input('destino')

    os.system('clear')

    Reservas.voosRegistrados.append(Voos(num, origem, destino))


def menuConsultarVoo():
    mostrarVoos(Reservas.voosRegistrados)
    input()
    os.system('clear')

# def menuCancelarVoo():

def mostrarVoos(lista):
    print('----------------------------')
    for num, voo in enumerate(lista):
        print(num, voo.numeroDeVoo)
    print('----------------------------')