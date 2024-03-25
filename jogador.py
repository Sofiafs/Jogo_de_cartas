class Jogador:
    def __init__(self,nome):
        self.nome = nome
        self.quant = []

    def receber_carta(self, cartas):
        print(self.nome, " recebeu 7 cartas!")
        self.quant = cartas

    def mostrar_carta(self, quant):
        print ("Mostrar cartas: ", quant)
