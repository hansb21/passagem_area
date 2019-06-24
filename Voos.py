import os

import Reservas

class Voos:
    def __init__(self, num):
        self.tipo = 'fretado'

        self.origem = 'a'
        self.destino = 'b'
        self.numeroDeVoo = num

        self.numeroAssentos = 10
        self.assentosDisponiveis = self.numeroAssentos
        
        self.passageiros = []
        self.quantidadeDePassagens = []
        self.passageirosAtuais = []

    def removerPassageiro(self, passageiro):
        for num, cont in enumerate(self.passageiros):
            if cont == passageiro:
                self.passageiros.pop(num)
                self.quantidadeDePassagens.pop(num)

    def GetinformacoesDeVoo(self, num):
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


        # self.passageiros.append(cliente)
        # cliente.voosComprados.append(self)

        Reservas.passagensCompradas.append({'voo': self, 'cliente': cliente, 'assentos': numPassagens})
        print(Reservas.passagensCompradas)
