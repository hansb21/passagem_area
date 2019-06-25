import os

import reservas

def menuCliente(cliento):
    global cliente
    cliente = cliento

    print(cliente.nome)
    while True:
        print('Cliente')
        opcao = input('cadastrar, consultar, cancelar, voltar')
        os.system('clear')

        if opcao == '0':
            menuCadastrarPassagem()
        elif opcao == '1':
            menuConsultarPassagem()
        elif opcao == '2':
            menuCancelarPassagem()
        elif opcao == 'v':
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
