import os

import reservas
from Voos import *

class Transporte(Voos):
    def __init__(self, num, origem, destino, horario):
        Voos.__init__(self, num, origem, destino, horario)
        self.tipo = 'Cargueiro'
        self.pesoMaximo = 1000
        self.__pesoDisponivel = 0
        self.__pesoAtual = 0
    
    def getPesoDisponivel(self):
        for i in reservas.passagensCompradas:
            if i['voo'] == self:
                pesoAtual += i['peso']               

        return (self.pesoMaximo - self.__pesoAtual)

    def mostrarInformacoes(self):
        margem = ' ' * 5
    
        print()
        print(f'{margem} Número do Voo:.......{self.numeroDeVoo}')
        print(f'{margem} Tipo:................{self.tipo}       ')
        print(f'{margem} Horário:.............{self.horario[0]}:{self.horario[1]}')
        print(f'{margem} Peso Máximo:.........{self.pesoMaximo} Ton')
        print(f'{margem} Origem:..............{self.origem}     ')
        print(f'{margem} Destino:.............{self.destino}    ')
        print()
        
    def reservarPassagem(self, cliente):
        os.system('clear')

        print(f'Tipo: Avião {self.tipo} \n')
        print('quanto pesa sua carga?')
        pesoCarga = int(input())

        if pesoCarga > self.getPesoDisponivel():
            input('Não há espaço disponível para sua carga')
            return

        preco = pesoCarga * reservas.precoTransporte / self.pesoMaximo

        while True:
            print(f'o preço da passagem é {preco}, deseja continuar?')
            print('s/n')
            opcao = input().lower()
            os.system('clear')

            if opcao == 's':
                break
            if opcao == 'n':
                return
                
        reservas.novaPassagem({'voo': self, 'cliente': cliente, 'peso': pesoCarga})
