import os

import reservas
from Voos import *

class Transporte(Voos):
    def __init__(self, num, origem, destino, pesoMaximo):
        Voos.__init__(self, num, origem, destino)
        self.tipo = 'de carga'
        self.pesoMaximo = pesoMaximo
    
    def getPesoDisponivel(self):
        pesoAtual = 0
        for i in reservas.passagensCompradas:
            if i['voo'] == self:
                pesoAtual += i['peso']
        return self.pesoMaximo - pesoAtual

    def mostrarInformacoes(self, num):
        margem = ' ' * 5
    
        print(f'{num}{margem}Número do Voo: {self.numeroDeVoo}')
        print(f'{margem} Tipo: {self.tipo}')
        print(f'{margem} Origem:  {self.origem}')
        print(f'{margem} Destino: {self.destino}')
        print('')

    def reservarPassagem(self, cliente):
        os.system('clear')

        print(f'Tipo: Avião {self.tipo}')
        print('quanto pesa sua carga?')
        pesoCarga = int(input())

        if pesoCarga > self.getPesoDisponivel():
            print('Não há espaço disponível para sua carga')
            input()
            return

        preco = pesoCarga*100 / self.pesoMaximo

        while True:
            print(f'o preço da passagem é {preco}, deseja continuar?')
            opcao = input()
            os.system('clear')

            if opcao == 's':
                break
            if opcao == 'n':
                return
                
        reservas.novaPassagem({'voo': self, 'cliente': cliente, 'peso': pesoCarga})
