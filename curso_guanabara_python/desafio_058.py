"""Melhore o jogo do DESAFIO_028 onde o computador vai "pensar" em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final, quantos palpites foram necessários para vencer!
"""

from random import randint
from time import sleep

computador = randint(0, 10) # Faz o computador "PENSAR"

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10, tente adivinhar...')
print('-=-' * 20)
jogador = 0 # variavel jogador que começa zerada
tentativas = 0 # variavel para acumular quantidade de tentativas
while jogador != computador:
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(2)
    tentativas += 1 # Cada jogada que o jogador fizer e não vencer, vai ser acumulada na variável
    if jogador == computador:
        print('PARABÉNS! Você conseguiu me vencer!')
        print(f'Para vencer de mim foram necessárias {tentativas} tentativas!')
    else:
        print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')
    # if jogador == computador:
    #     print(f'Para vencer de mim foram necessárias {tentativas} tentativas!')