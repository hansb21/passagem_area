import os
from colorama import init
from termcolor import colored

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
        input(colored('Já existem 3 vôos cadastrados.', 'red'))
        return

    numeroVoo = setNumeroVoo()
    horario = setHorario()

    while True:
        origem  = input(colored('Origem:  ', 'blue'))
        if origem == '':
            print(colored('Por favor coloque uma origem valida.', 'red'))
        else:
            break
    while True:
        destino = input(colored('Destino: ', 'blue'))
        if destino == '':
            print(colored('Por favor entre um destino valido.', 'red'))
        else:
            break
    os.system('clear')

    tipo = setTipoVoo()

    if tipo == 0:
        novoVoo = Transporte(numeroVoo, origem, destino, horario)
        novoVoo.pesoMaximo = int(input(colored('Peso maximo: ', 'blue')))

    elif tipo == 1:
        while True:
            assentos = int(input('Número de assentos: '))
            if assentos <= 0:
                print('Número invalido, tente novamente')
            else:
                break
        novoVoo = Comercial(numeroVoo, origem, destino, horario, assentos)

    elif tipo == 2:
        novoVoo = Fretado(numeroVoo, origem, destino, horario)
        while True:
            assentos = int(input('Número de assentos: '))
            if assentos <= 0:
                print('Número invalido, tente novamente')
            else:
                break
        novoVoo.numeroAssentos = assentos
        while True:
            distancia = int(input('Distância: '))
            if distancia <= 0:
                print('Distância invalido, tente novamente')
            else:
                break
        novoVoo.distancia = distancia

    reservas.novoVoo(novoVoo)

def menuConsultarVoo():
    mostrarVoos(reservas.voosRegistrados)
    vooEscolhido = input(colored('Digite o número do vôo para verificar passageiros: ', 'blue'))

    for voo in reservas.voosRegistrados:
        if voo.numeroDeVoo == vooEscolhido:
            if voo.getPassageiros() == []:
                input(colored('Não há passageiros neste vôo.', 'red'))
                return

            for i in voo.getPassageiros():
                print(colored(f'Nome:.......{i.nome}', 'blue'))
                print(colored(f'CPF:........{i.cpf}', 'blue'))
                print('')
            input()
            return
    
def menuCancelarVoo():
    mostrarVoos(reservas.voosRegistrados)
    while True:
        vooEscolhido = input(colored('Digite o número do vôo que deseja cancelar: ', 'blue'))
        if len(vooEscolhido) != 5:
            print('Número invalido. ')
        else:
            break
    for voo in reservas.voosRegistrados:
        if voo.numeroDeVoo == vooEscolhido:
            reservas.cancelarPassagem(voo)
        else:
            print(colored('Esse vôo não existe.', 'red'))
    # reservas.cancelarVoo()


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
        num = input(colored('Número do vôo: ', 'blue'))
        if len(num) != 5:
            print(colored('O número precisa ter 5 dígitos.', 'red'))
        else:
            for voo in reservas.voosRegistrados:
                if voo.numeroDeVoo == num:
                    numValido = False
            if numValido:
                break
            else:
                print(colored('Um vôo com esse número já existe.', 'red'))

    os.system('clear')
    return num


def setHorario():
    while True:
        tempo = input(colored('Horario (HH:MM): ', 'blue'))
        if len(tempo) == 5 and tempo[2] == ':':
            time = tempo.split(':')
            time[0] = int(time[0])
            time[1] = int(time[1])
            
            if 0 <= time[0] < 24  and 0 <= time[1] < 60:
                return time
        print(colored('Insira um horário válido. ', 'red'))

