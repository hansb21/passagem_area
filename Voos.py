import os

import Reservas

class Voos:
    def __init__(self, num, origem, destino):
        self.tipo = 'fretado'

        self.origem = destino
        self.destino = destino
        self.numeroDeVoo = num

        self.numeroAssentos = 10
        self.assentosDisponiveis = self.numeroAssentos

    #     self.passageiros = []
    #     self.quantidadeDePassagens = []
    #     self.passageirosAtuais = []

    # # def removerPassageiro(self, passageiro):
    # #     for num, cont in enumerate(self.passageiros):
    # #         if cont == passageiro:
    # #             self.passageiros.pop(num)
    # #             self.quantidadeDePassagens.pop(num)

    def getInformacoes(self, num):
        margem = ' ' * 5
    
        print(f'{num}{margem}Número do Voo: {self.numeroDeVoo}')
        print(f'{margem} Tipo: {self.tipo}')
        print(f'{margem} Origem:  {self.origem}')
        print(f'{margem} Destino: {self.destino}')
        print('')

    def getPassageiros(self):
        passag = []
        for i in Reservas.passagensCompradas:
            if i['voo'] == self:
                passag.append(i['cliente'])
        return passag

    def getAssentosDisponiveis(self):
        passagensOcupadas = 0
        for i in Reservas.passagensCompradas:
            if i['voo'] == self:
                passagensOcupadas += i['assentos']
        return self.numeroAssentos - passagensOcupadas

    def reservarPassagem(self, cliente):
        os.system('clear')

        print(f'Tipo: Avião {self.tipo}')
        print('Quantas passagens deseja reservar?')
        numPassagens = int(input())

        if numPassagens > self.getAssentosDisponiveis():
            print('Não há mais assentos disponíveis')
        else:
            preco = numPassagens*100
            print(f'o preço da passagem é {preco}')

            # self.passageiros.append(cliente)
            # cliente.voosComprados.append(self)

            Reservas.passagensCompradas.append({'voo': self, 'cliente': cliente, 'assentos': numPassagens})
            print(Reservas.passagensCompradas)
