import os

import reservas
from Fretado import *
from Comercial import *
from Transporte import *

def menuOperador():
    while True:
        print('Operador')
        opcao = input('cadastrar, consultar, cancelar, voltar')
        os.system('clear')

        if opcao == '0':
            menuCadastrarVoo()
        elif opcao == '1':
            menuConsultarVoo()
        elif opcao == '2':
            menuCancelarVoo()
        else:
            break
        
def menuCadastrarVoo():
    tipo = input('tipo')
    num = input('num')
    origem = input('origem')
    destino = input('destino')
    os.system('clear')

    if tipo == 'de carga':
        peso = input('peso maximo')
        novoVoo = Transporte(num, origem, destino, peso)
    elif tipo == 'comercial':
        novoVoo = Comercial(num, origem, destino)
    elif tipo == 'fretado':
        novoVoo = Fretado(num, origem, destino)
        
    reservas.novoVoo(novoVoo)


def menuConsultarVoo():
    mostrarVoos(reservas.voosRegistrados)
    input()
    os.system('clear')

def menuCancelarVoo():
    mostrarVoos(reservas.voosRegistrados)
    opcao = int(input())

    vooCancelado = reservas.voosRegistrados[opcao]
    reservas.cancelarVoo(vooCancelado)

def mostrarVoos(lista):
    print('----------------------------')
    for num, voo in enumerate(lista):
        voo.mostrarInformacoes(num)
    print('----------------------------')