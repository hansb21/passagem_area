import os

from Voos import *

class Fretado(Voos):
    def __init__(self, num, origem, destino, horario):
        Voos.__init__(self, num, origem, destino, horario)
        self.tipo = 'Fretado'
        self.numeroAssentos = 100
        self.distancia = 1000
        self.__passagensOcupadas = 0

    def mostrarInformacoes(self):
        margem = ' ' * 5

        print()
        print(f'{margem} Número do Voo:.......{self.numeroDeVoo}   ')
        print(f'{margem} Tipo:................{self.tipo}          ')
        print(f'{margem} Horário:.............{self.horario[0]}:{self.horario[1]}')
        print(f'{margem} Número de assentos:..{self.numeroAssentos}')
        print(f'{margem} Origem:..............{self.origem}        ')
        print(f'{margem} Destino:.............{self.destino}       ')
        print(f'{margem} Distância:...........{self.distancia} Km  ')
        print()

    def getAssentosDisponiveis(self):
        self.__passagensOcupadas = 0
        for i in reservas.passagensCompradas:
            if i['voo'] == self:
                self.__passagensOcupadas += i['assentos']
        return (self.numeroAssentos - self.__passagensOcupadas)

    def reservarPassagem(self, cliente):
        os.system('clear')

        print(f'Tipo: Avião {self.tipo} \n')
        print('Quantas passagens deseja reservar?')
        numPassagens = int(input())

        if numPassagens > self.getAssentosDisponiveis():
            input('Não há mais assentos disponíveis')
            return

        preco = (numPassagens * reservas.precoFretado) + (self.distancia * reservas.precoPorKm / self.numeroAssentos)
        
        while True:
            os.system('clear')

            print(f'o preço da passagem é R$ {preco:.2f}, deseja continuar?')
            print('s/n')
            opcao = input().lower()

            if opcao == 's':
                break
            if opcao == 'n':
                return

        reservas.novaPassagem({'voo': self, 'cliente': cliente, 'assentos': numPassagens})
        input('Vôo cadastrado com sucesso!')