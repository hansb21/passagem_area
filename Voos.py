import os

import reservas

class Voos:
    def __init__(self, num, origem, destino, horario):
        self.origem = origem
        self.destino = destino
        self.numeroDeVoo = num
        self.horario = horario

    def getPassageiros(self):
        passag = []
        for i in reservas.passagensCompradas:
            if i['voo'] == self:
                passag.append(i['cliente'])
        return passag

