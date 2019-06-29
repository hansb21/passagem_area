voosRegistrados = []
clientesRegistrados = []
passagensCompradas = []

precoComercial = 300
precoTransporte = 1000
precoFretado = 100
precoPorKm = 10

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