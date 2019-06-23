import os

from Voos import *

class Transporte(Voos):
    def __init__(self, num):
        Voos.__init__(self, num)
        self.tipo = 'de carga'
        self.pesoMaximoTon = 1000
        self.pesoDisponivel = self.pesoMaximoTon

    def reservarPassagem(self, cliente):
        os.system('clear')

        print(f'Tipo: Avião {self.tipo}')
        print('quanto pesa sua carga?')
        pesoCarga = int(input())

        if pesoCarga > self.pesoDisponivel:
            print('Não há espaço disponível para sua carga')
            input()
            return


        preco = pesoCarga*100 / self.pesoMaximoTon
        print(f'o preço da passagem é R$ {preco:.2f}')
        print('deseja continuar')
        resposta = input()

        if resposta == 's':
            self.passageiros.append(cliente)
            cliente.voosComprados.append(self)
        else:
            menuConsultar()
