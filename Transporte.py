import os
from colorama import init
from termcolor import colored

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
        self.__pesoAtual = 0
        for i in reservas.passagensCompradas:
            if i['voo'] == self:
                self.__pesoAtual += i['peso']               

        return (self.pesoMaximo - self.__pesoAtual)

    def mostrarInformacoes(self):
        margem = ' ' * 5
    
        print()
        print(f'{margem} Número do Voo:.......{self.numeroDeVoo}')
        print(f'{margem} Tipo:................{self.tipo}       ')
        print(f'{margem} Horário:.............{self.horario[0]}:{self.horario[1]}')
        print(f'{margem} Peso Máximo:.........{self.pesoMaximo} Kg')
        print(f'{margem} Origem:..............{self.origem}     ')
        print(f'{margem} Destino:.............{self.destino}    ')
        print()
        
    def reservarPassagem(self, cliente):
        os.system('clear')

        print(colored(f'Tipo: Avião {self.tipo} \n', 'green'))
        print(colored('quanto pesa sua carga?', 'green'))
        while True:
            pesoCarga = int(input())
            if pesoCarga < 0:
                print(colored('Carga invalida.', 'red'))
            else:
                break
        if pesoCarga > self.getPesoDisponivel():
            input(colored('Não há espaço disponível para sua carga', 'red'))
            return

        preco = pesoCarga * reservas.precoTransporte / self.pesoMaximo

        while True:
            print(colored(f'O preço da passagem é R$ {preco:.2f}, deseja continuar?', 'green'))
            print(colored('S/N', 'green'))
            opcao = input().lower()
            os.system('clear')

            if opcao == 's':
                break
            if opcao == 'n':
                return
                
        reservas.novaPassagem({'voo': self, 'cliente': cliente, 'peso': pesoCarga})
        input(colored('Vôo cadastrado com sucesso!', 'green'))
