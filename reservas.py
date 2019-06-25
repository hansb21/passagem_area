from Transporte import *
from Comercial import *
from Fretado import *
from Cliente import *

voosRegistrados = [Fretado(111, 'A', 'B'), Comercial(222, 'B', 'C'), Transporte(333, 'C', 'D', 20000)]
clientesRegistrados = [Cliente('Andre', 2032130192)]

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
    voosRegistrados.append(voosRegistrados.index(voo))

def novaPassagem(passagem):
    passagensCompradas.append(passagem)

def cancelarPassagem(voo):
    for i in passagensCompradas:
        if i['voo'] == voo:
            passagensCompradas.pop(passagensCompradas.index(i))