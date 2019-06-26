from Transporte import *
from Comercial import *
from Fretado import *

voosRegistrados = [Fretado(11111, 'A', 'B', '11:30'), Comercial(22222, 'B', 'C', '11:30'), Transporte(33333, 'C', 'D', 20000, '11:30')]
clientesRegistrados = []

passagensCompradas = []

def acharCliente(nome, cpf):
    for i in clientesRegistrados:
        if i.nome == nome and i.cpf == cpf:
            return i
    else:
        return False

def novoCliente(cliente):
    clientesRegistrados.append(cliente)

def novoVoo(voo):
    voosRegistrados.append(voo)

def cancelarVoo(voo):
    cancelarPassagem(voo)    
    voosRegistrados.pop(voosRegistrados.index(voo))

def novaPassagem(passagem):
    passagensCompradas.append(passagem)

def cancelarPassagem(voo):
    for i in passagensCompradas:
        if i['voo'] == voo:
            passagensCompradas.pop(passagensCompradas.index(i))