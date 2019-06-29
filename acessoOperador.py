import os

import reservas
from interfaces import *
from Fretado import *
from Comercial import *
from Transporte import *

# principais
def menuOperador():
    while True:
        mostrarMenuOperador()
        opcao = input()
        
        if opcao == '0':
            menuCadastrarVoo()
        elif opcao == '1':
            menuConsultarVoo()
        elif opcao == '2':
            menuCancelarVoo()
        elif opcao == '3':
            break
        
def menuCadastrarVoo():
    os.system('clear')

    if len(reservas.voosRegistrados) >= 3:
        input('Já existem 3 vôos cadastrados.')
        return

    numeroVoo = setNumeroVoo()
    horario = setHorario()
    origem  = input('Origem:  ')
    destino = input('Destino: ')
    os.system('clear')

    tipo = setTipoVoo()

    if tipo == 0:
        novoVoo = Transporte(numeroVoo, origem, destino, horario)
        novoVoo.pesoMaximo = int(input('Peso maximo: '))

    elif tipo == 1:
        novoVoo = Comercial(numeroVoo, origem, destino, horario)
        novoVoo.numeroAssentos = int(input('Número de assentos: '))

    elif tipo == 2:
        novoVoo = Fretado(numeroVoo, origem, destino, horario)
        novoVoo.numeroAssentos = int(input('Número de assentos: '))
        novoVoo.distancia = int(input('Distância: '))

    reservas.novoVoo(novoVoo)

def menuConsultarVoo():
    mostrarVoos(reservas.voosRegistrados)
    vooEscolhido = input('Digite o número do vôo para verificar passageiros: ')

    for voo in reservas.voosRegistrados:
        if voo.numeroDeVoo == vooEscolhido:
            if voo.getPassageiros() == []:
                input('Não há passageiros neste vôo')
                return

            for i in voo.getPassageiros():
                print(f'Nome:.......{i.nome}')
                print(f'CPF:........{i.cpf}')
                print()
            input()
            return
    
def menuCancelarVoo():
    mostrarVoos(reservas.voosRegistrados)
    vooEscolhido = input('Digite o número do vôo que deseja cancelar: ')

    for voo in reservas.voosRegistrados:
        if voo.numeroDeVoo == vooEscolhido:
            reservas.cancelarVoo(voo)
            return
    else:
        input('Não foi possível cancelar esse Vôo')


# Úteis
def setTipoVoo():
    tipo = ''
    while tipo not in range(3):
        mostrarTiposVoo()
        tipo = int(input())
        
    os.system('clear')
    return tipo

def setNumeroVoo():
    while True:
        numValido = True
        num = input('Número do vôo: ')
        if len(num) != 5:
            print('O número precisa ter 5 dígitos')
        else:
            for voo in reservas.voosRegistrados:
                if voo.numeroDeVoo == num:
                    numValido = False
            if numValido:
                break
            else:
                print('Esse número já existe')

    os.system('clear')
    return num


def setHorario():
    while True:
        tempo = input('Horario (HH:MM):')
        if len(tempo) == 5 and tempo[2] == ':':
            time = tempo.split(':')
            return time