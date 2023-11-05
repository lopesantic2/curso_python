"""Escreva um programa que faça o computador 'pensar' em um número entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu!"""

import random

num = int(input('Insira um número entre 0 e 5: '))
lista = [1, 2, 3, 4, 5]

if num <= 5:
    lista = random.choice(lista)
    print(f'O número era {lista}')
    if num == lista:
        print('Você acertou!')
    else:
        print('Tente de novo!')

else:
    print('Somente números de 1 à 5!')