import random

list = [1, 2, 3, 4, 5, 6, 7]
quant = []
class Baralho:
    def __init__(self):
        naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
        valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
        self.cartas = [{'valor': v, 'naipe': n} for n in naipes for v in valores]
    def embaralhar(self):
        random.shuffle(self.cartas)
    
    def distribuir_carta(self):
        if len(self.cartas) == 0:
            return None
        return self.cartas.pop()
    
'''b01 = Baralho()
b01.embaralhar()
cd01 = Baralho.distribuir_carta(b01)
print(cd01)'''