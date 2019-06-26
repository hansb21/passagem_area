import os

from Voos import *

class Fretado(Voos):
    def __init__(self, num, origem, destino):
        Voos.__init__(self, num, origem, destino)
        self.tipo = 'fretado'
        self.numeroAssentos = 10
        self.distancia = 2000

    def mostrarInformacoes(self, num):
        margem = ' ' * 5
    
        print(f'{num}{margem}Número do Voo: {self.numeroDeVoo}')
        print(f'{margem} Tipo: {self.tipo}')
        print(f'{margem} Origem:  {self.origem}')
        print(f'{margem} Destino: {self.destino}')
        print('')

    def getAssentosDisponiveis(self):
        passagensOcupadas = 0
        for i in reservas.passagensCompradas:
            if i['voo'] == self:
                passagensOcupadas += i['assentos']
        return (self.numeroAssentos - passagensOcupadas)

    def reservarPassagem(self, cliente):
        os.system('clear')

        print(f'Tipo: Avião {self.tipo}')
        print('Quantas passagens deseja reservar?')
        numPassagens = int(input())

        if numPassagens > self.getAssentosDisponiveis():
            print('Não há mais assentos disponíveis')
        else:
            preco = numPassagens*100 + self.distancia*0.02

            while True:
                print(f'o preço da passagem é {preco}, deseja continuar?')
                opcao = input()
                os.system('clear')

                if opcao == 's':
                    break
                if opcao == 'n':
                    return

            reservas.novaPassagem({'voo': self, 'cliente': cliente, 'assentos': numPassagens})