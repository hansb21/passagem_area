import os

from Voos import *

class Fretado(Voos):
    def __init__(self, num, origem, destino, horario):
        Voos.__init__(self, num, origem, destino, horario)
        self.tipo = 'fretado'
        self.__numeroAssentos = 10
        self.distancia = 2000
        self.__passagensOcupadas = 0

    def mostrarInformacoes(self, num):
        margem = ' ' * 5
    
        print(f'{num}{margem}Número do Voo: {self.numeroDeVoo}')
        print(f'{margem} Horário: {self.horario}')
        print(f'{margem} Tipo: {self.tipo}')
        print(f'{margem} Origem:  {self.origem}')
        print(f'{margem} Destino: {self.destino}')
        print('')

    def getAssentosDisponiveis(self):
        for i in reservas.passagensCompradas:
            if i['voo'] == self:
                self.__passagensOcupadas += i['assentos']
        return (self.__numeroAssentos - self.__passagensOcupadas)

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