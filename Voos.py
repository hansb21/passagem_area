import os

import reservas

class Voos:
    def __init__(self, num, origem, destino):
        self.origem = origem
        self.destino = destino
        self.numeroDeVoo = num

    def getPassageiros(self):
        passag = []
        for i in reservas.passagensCompradas:
            if i['voo'] == self:
                passag.append(i['cliente'])
        return passag

