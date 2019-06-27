import os

import reservas

class Voos:
    def __init__(self, num, origem, destino, horario):
        self.origem = origem
        self.destino = destino
        self.numeroDeVoo = num
        self.horario = horario
        self.__passageiros = []

    def getPassageiros(self):
        for i in reservas.passagensCompradas:
            if i['voo'] == self:
                self.__passageiros.append(i['cliente'])
        return self.__passageiros

