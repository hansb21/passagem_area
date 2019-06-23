import os
from termcolor import colored

class Voos:
    def __init__(self, num):
        self.tipo = 'fretado'

        self.origem = 'a'
        self.destino = 'b'
        self.numeroDeVoo = num

        self.numeroAssentos = 10
        self.assentosDisponiveis = self.numeroAssentos
        self.passageiros = []

    def removerPassageiro(self, passageiro):
        for num, cont in enumerate(self.passageiros):
            if cont == passageiro:
                self.passageiros.pop(num)

    def informacoesDeVoo(self, num):
        margem = ' ' * 5

        print(f'{num}{margem}Número do Voo: {self.numeroDeVoo}')
        print(f'{margem} Tipo: {self.tipo}')
        print(f'{margem} Origem:  {self.origem}')
        print(f'{margem} Destino: {self.destino}')
        print('')

    def reservarPassagem(self, cliente):
        os.system('clear')

        print(f'Tipo: Avião {self.tipo}')
        print('Quantas passagens deseja reservar?')
        numPassagens = int(input())

        preco = numPassagens*100
        print(f'o preço da passagem é {preco}')
        print('deseja continuar?')
        resposta = input()

        if resposta == 's':
            self.passageiros.append(cliente)
            cliente.voosComprados.append(self)
        else:
            menuConsultar()
