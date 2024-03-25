import baralho
import carta
import jogador

baralho_ = baralho.Baralho()
j01 = jogador.Jogador('Melissa')
j02 = jogador.Jogador('Sofia')
baralho_.embaralhar()

cartas01 = []
for i in cartas01:
    a = baralho.Baralho.distribuir_carta(j01)
    cartas01.append(a)

cartas02 = []
for i in cartas02:
    a = baralho.Baralho.distribuir_carta(j02)
    cartas01.append(a)

print('Carta do jogador 01:')
jogador.Jogador.mostrar_carta(j01, cartas01)

print(' ')

print('Carta do jogador 02: ')
jogador.Jogador.mostrar_carta(j02, cartas02)