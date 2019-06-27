import reservas

class Cliente:
    def __init__(self, nome, cpf ):
        self.nome = nome
        self.cpf = cpf
        

    def getVoosComprados(self):
        self.voosComprados = []
        for i in reservas.passagensCompradas:
            if i['cliente'] == self:
                self.voosComprados.append(i['voo'])
        return self.voosComprados
