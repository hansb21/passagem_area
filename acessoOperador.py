import os

import reservas
from Fretado import *
from Comercial import *
from Transporte import *

def menuOperador():
    while True:
        print('Operador')
        for i in ['0 - cadastrar', '1 - consultar', '2 - cancelar', '3 -voltar']:
            print(i)
        opcao = int(input('O que você deseja fazer? '))
        os.system('clear')
        
        if opcao == 0:
            menuCadastrarVoo()
        elif opcao == 1:
            menuConsultarVoo()
        elif opcao == 2:
            menuCancelarVoo()
        else:
            break
        
def menuCadastrarVoo():
    while True:
        for i in ['0 - De carga', '1 - Comercial', '2 - fretado']:
            print(i)
        tipo = int(input('Tipo do vôo: '))
        if tipo not in range(0, 3):
            print('Tipo de vôo invalido. ')
        else:
            break
    while True:
        num = input('Número do vôo: ')
        if len(num) != 5:
            print('Número invalido.')
        else:
            break
            
    origem = input('Origem: ')
    destino = input('Destino: ')
    horario = input('Horario: ')
    os.system('clear')

    if tipo == 0:
        peso = int(input('Peso maximo: '))
        novoVoo = Transporte(num, origem, destino, peso, horario)
    elif tipo == 1:
        novoVoo = Comercial(num, origem, destino, horario)
    elif tipo == 2:
        novoVoo = Fretado(num, origem, destino, horario)
        
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