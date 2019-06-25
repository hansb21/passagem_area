import os

from Voos import *

class Comercial(Voos):
    def __init__(self, num, origem, destino):
        Voos.__init__(self, num, origem, destino)
        self.tipo = 'comercial'
        self.numeroAssentos = 10
        self.primeiraClasse = int(self.numeroAssentos * 0.2)
        self.classeEconomica = self.numeroAssentos - self.primeiraClasse

    def mostrarInformacoes(self, num):
        margem = ' ' * 5
        
        print(f'{num}{margem}Número do Voo: {self.numeroDeVoo}')
        print(f'{margem} Tipo: {self.tipo}')
        print(f'{margem} Origem:  {self.origem}')
        print(f'{margem} Destino: {self.destino}')
        print('')

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
        print(f'Tipo: Avião {self.tipo}')

        print('Quantas passagens deseja reservar?')
        numPassagens = int(input())

        print('Primeira Classe ou Economica: ')
        opcao = input()
        opcap = opcao.lower()
        global classe

        if opcao == 'primeiro':
            classe = 'primeira'
        elif opcao == 'economica':
            classe = 'economica'

        if numPassagens > self.getAssentosDisponiveis(classe):
            print('Não há mais assentos disponíveis')

            if classe == 'primeira':
                classe = 'economica'
            else:
                classe = 'primeira'

            if numPassagens > self.getAssentosDisponiveis(classe):
                return
            else:
                while True:
                    print(f'Deseja ser encaminhado para a classe {classe}?')
                    opcao = input()
                    os.system('clear')

                    if opcao == 'n':
                        return
                    elif opcao == 's':
                        break

        preco = numPassagens*100

        while True:
            print(f'o preço da passagem é {preco}, deseja continuar?')
            opcao = input()
            os.system('clear')

            if opcao == 's':
                break
            if opcao == 'n':
                return
            
        reservas.novaPassagem({'voo': self, 'cliente': cliente, 'assentos': numPassagens, 'classe':classe})
        