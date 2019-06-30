import os
from colorama import init
from termcolor import colored
from Voos import *
from interfaces import *

class Comercial(Voos):
    def __init__(self, num, origem, destino, horario, assentos):
        Voos.__init__(self, num, origem, destino, horario)
        self.tipo = 'Comercial'
        self.numeroAssentos = assentos
        self.primeiraClasse = int(self.numeroAssentos * 0.2)
        self.classeEconomica = self.numeroAssentos - self.primeiraClasse

    def mostrarInformacoes(self):
        margem = ' ' * 5

        print()
        print(f'{margem} Número do Voo:.......{self.numeroDeVoo}')
        print(f'{margem} Tipo:................{self.tipo}       ')
        print(f'{margem} Horário:.............{self.horario[0]}:{self.horario[1]}')
        print(f'{margem} Número de assentos:..{self.numeroAssentos}')
        print(f'{margem} Origem:..............{self.origem}     ')
        print(f'{margem} Destino:.............{self.destino}    ')
        print()

    def getAssentosDisponiveis(self, classe):
        passagensOcupadas = 0

        for i in reservas.passagensCompradas:
            if i['voo'] == self and i['classe'] == classe:
                passagensOcupadas += i['assentos']
        
        if classe == 'primeira':
            return self.primeiraClasse - passagensOcupadas
        else:
            return self.classeEconomica - passagensOcupadas

    def reservarPassagem(self, cliente):
        os.system('clear')
        print(colored(f'Tipo: Avião {self.tipo}', 'green'))
        while True:
            print('Quantas passagens deseja reservar?')
            numPassagens = int(input())
            if numPassagens <= 0:
                print('Número de passagens invalido.')
            else:
                break
            
        global classe

        while True:
            print(colored('0 - Primeira Classe.', 'green'))
            print(colored('1 - Economica.''green'))
            opcao = input()

            if opcao == '0':
                classe = 'primeira'
                break
            elif opcao == '1':
                classe = 'economica'
                break

        # deus que me perdoe por essa gambiarra
        if numPassagens > self.getAssentosDisponiveis(classe):
            input('Desculpe, não há mais assentos disponíveis nesse vôo.')

            if classe == 'primeira':
                classe = 'economica'
            else:
                classe = 'primeira'

            if numPassagens > self.getAssentosDisponiveis(classe):
                return
            else:
                while True:
                    print(f'Deseja ser encaminhado para a classe {classe}?')
                    print('S/N')

                    opcao = input()
                    os.system('clear')

                    if opcao == 'n':
                        return
                    elif opcao == 's':
                        break 

        mostrarRestricoesAlimentares()
        while True:
            restricaoAlimentar = int(input())
            if restricaoAlimentar < 0:
                print(colored('Número invalido.','red'))
            else:
                break
            


        preco = numPassagens * reservas.precoComercial
        preco += (preco * 0.05) * restricaoAlimentar
        
        if classe == 'primeira':
            preco += 100
        if self.numeroAssentos >= 100:
            preco -= preco * 0.15
        if self.horario[0] < 5 or self.horario[0] > 22:
            preco -= preco * 0.25

        while True:
            print(colored(f'o preço da passagem é R$ {preco:.2f}, deseja continuar?','green'))
            print(colored('S/N','green'))
            opcao = input().lower()
            os.system('clear')

            if opcao == 's':
                break
            if opcao == 'n':
                return
                classe = 'economica'
            else:
                classe = 'primeira'
            
        reservas.novaPassagem({'voo': self, 'cliente':cliente, 'assentos':numPassagens, 'classe':classe})
        print(colored('Vôo cadastrado com sucesso!', 'red'))
        input(colored('Boa viagem!', 'red'))