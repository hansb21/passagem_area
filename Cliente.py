# class Cliente:
#     def __init__(self, nome, cpf):
#         self.nome = nome
#         self.cpf  = cpf
#         self.voosComprados = []

#     def removerVoo(self, vooPassagemCancelada):
#         for num, cont in enumerate(self.voosComprados):
#             if cont(1) == vooPassagemCancelada:
#                 self.voosComprados.pop(num)
class Clientes:
    def __init__(self):
        self.__clientes = {}
        self.__pins= {}
    def __len__(self):
        return len(self.__clientes)
    
    def __getitem__(self, position):
        return self.__clientes[position]
    
    def adicionar_Cliente(self, nome, cpf):
        pin = (len(self.__clientes)+1109)
        self.__pins[pin] = True
        self.__clientes[id] = [nome, cpf, []]
        print('Cliente cadastrado com sucesso')
        print('Esse é seu pin de login para comprar novas passagens, anote-o em segurança. ')
        print ('{}'.format(pin))

    def remover_Cliente(self):
        while True:
            login = int(input('Digite seu login: '))
            print(self.__clientes[login - 1110])
            escolha = input("Esse é você?: ")
            if escolha in ['s', 'S', 'y', 'Y']:
                del self.__clientes[login - 1110]
                break
            else:
                print('Digite seu login novamente: ')


