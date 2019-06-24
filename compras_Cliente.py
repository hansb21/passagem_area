from Cliente import *
from Voos import *
from Reservas import *
from colorama import init
from termcolor import colored
import time
import os

reserva = []

cliente = clientesRegistrados[0]

# # Menu principal com 4 opções:
# 1 - Cadastrar
# 2 - Consultar
# 3 - Remover
# 4 - Sair



def menuPrincipal():
    os.system('clear')
    while True:
        print('*' * 51)
        print(colored('Bem vindo ao sistema de passagens aéreas Sputnik 1.', 'blue'))
        print('*' * 51)
        print(' ')

        print(colored('1 - Cadastrar', 'blue'))
        print(colored('2 - Consultar', 'blue'))
        print(colored('3 - Remover','blue'))
        print(colored('4 - Sair', 'blue'))
        print(' ')
        resposta = int(input(colored('Escolha uma opção: ','blue')))

        if resposta == 1:
            os.system('clear')

            print('*' * 51)
            print(' ')
            print(colored('1 - Cadastrar', 'red'))
            print(colored('2 - Consultar', 'blue'))
            print(colored('3 - Remover','blue'))
            print(colored('4 - Sair', 'blue'))
            print(' ')
            time.sleep(1)
            menuCadastrar()
            break
        elif resposta == 2:
            os.system('clear')
            print('*' * 51)
            print(' ')
            print(colored('1 - Cadastrar', 'blue'))
            print(colored('2 - Consultar', 'red'))
            print(colored('3 - Remover','blue'))
            print(colored('4 - Sair', 'blue'))
            print(' ')
            time.sleep(1)
            menuConsultar()
            break
        elif resposta == 3:
            os.system('clear')
            print('*' * 51)
            print(' ')
            print(colored('1 - Cadastrar', 'blue'))
            print(colored('2 - Consultar', 'blue'))
            print(colored('3 - Remover','red'   ))
            print(colored('4 - Sair', 'blue'))
            print(' ')
            time.sleep(1)
            menuRemover()
            break
        elif resposta == 4:
            os.system('clear')
            print('*' * 51)
            print(' ')
            print(colored('1 - Cadastrar', 'blue'))
            print(colored('2 - Consultar', 'blue'))
            print(colored('3 - Remover','blue'))
            print(colored('4 - Sair ', 'red'   ))
            time.sleep(1)
            os.system('clear')
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
