import Reservas

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf  = cpf
        self.voosComprados = []

    def removerVoo(self, vooPassagemCancelada):
        for num, cont in enumerate(self.voosComprados):
            if cont(1) == vooPassagemCancelada:
                self.voosComprados.pop(num)

    def getVoosComprados(self):
        voosComprad = []

        for i in Reservas.passagensCompradas:
            if i['cliente'] == self:
                voosComprad.append(i['voo'])
        return voosComprad

        print('não deu')
