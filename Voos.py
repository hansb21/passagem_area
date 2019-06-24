class Voos:
    def __init__(self, num):
        self.origem = 'a'
        self.destino = 'b'
        self.numeroDeVoo = num

        self.numeroMaximoPassageiros = 10
        self.__passageiros = []
        self.quantidadeDePassagens = []
        self.passageirosAtuais = []
    def __len__(self):
        return len(self.__passageiros)
    def __getobject__(self, position):
        return self.__passageiros[position]
    
    def removerPassageiro(self, passageiro):
        for num, cont in enumerate(self.passageiros):
            if cont == passageiro:
                self.__passageiros.pop(num)
                self.quantidadeDePassagens.pop(num)


    # def getNumPassageiros():
    #     return sum(quantidadeDePassagens) #Só usar o len() pra receber o tamanho da lista de passageiros

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