"""Escreva um programa que faça o computador 'pensar' em um número entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu!"""

from random import randint
from time import sleep
#
# num = int(input('Insira um número entre 0 e 5: '))
# lista = [1, 2, 3, 4, 5]
#
# if num <= 5:
#     lista = random.choice(lista)
#     print(f'O número era {lista}')
#     if num == lista:
#         print('Você acertou!')
#     else:
#         print('Tente de novo!')
#
# else:
#     print('Somente números de 1 à 5!')

computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')