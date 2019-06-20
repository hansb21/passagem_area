class Voos:
    def __init__(self, num):
        self.origem = 'a'
        self.destino = 'b'
        self.numeroDeVoo = num

        self.numeroMaximoPassageiros = 10
        self.passageiros = []
        self.quantidadeDePassagens = []

    def removerPassageiro(self, passageiro):
        for num, cont in enumerate(self.passageiros):
            if cont == passageiro:
                self.passageiros.pop(num)
                self.quantidadeDePassagens.pop(num)

    def getNumPassageiros():
        return sum(quantidadeDePassagens)

    def reservarPassagem(self, cliente):
        print('Tipo: Avião Fretado')
        numPassagens = int(input('Quantas passagens deseja reservar?\n'))
        preco = numPassagens*100

        resposta = input(f'o preço da passagem é {preco} \ndeseja continuar? \n')

        if resposta == 's':
            self.passageiros.append(cliente)
            self.quantidadeDePassagens.append(numPassagens)
            cliente.voosComprados.append(self)
        else:
            menuConsultar()
