#!bin/python3
from random import randint
print('')
print('----- JOGO PEDRA, PAPEL E TESOURA -----')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
player = input('Selecione um: ')

if player == '1':
    player = "Pedra"
elif player == '2':
    player = "Papel"
else:
    player = "Tesoura"

escolha = randint(1, 3)

if escolha == 1:
    computador = 'Pedra'
elif escolha == 2:
    computador = 'Papel'
else:
    computador = 'Tesoura'

print(f"{player} vs {computador}")

if player == computador:
    print("EMPATE TÉCNICO!!")
elif player == 'Pedra' and computador == 'Tesoura':
    print('VOCÊ GANHOU!!')
elif player == 'Pedra' and computador == 'Papel':
    print('VOCÊ PERDEU!!')
elif player == 'Tesoura' and computador == 'Pedra':
    print('VOCÊ PERDEU!!')
elif player == 'Tesoura' and computador == 'Papel':
    print('VOCÊ GANHOU!!')
elif player == 'Papel' and computador == 'Tesoura':
    print('VOCÊ PERDEU!!')
elif player == 'Papel' and computador == 'Pedra':
    print('VOCÊ GANHOU!!')
