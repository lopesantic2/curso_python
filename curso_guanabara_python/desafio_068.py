"""
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando
o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

print('-=-'*8)
print(' JOGO DO PAR OU ÍMPAR ')
print('-=-'*8)

vitoria = 0
par = 'P'
impar = 'I'
soma = 0
while True:
    jogador = int(input('Insira um valor entre 1 e 10: '))
    parimpar = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    computador = randint(0, 11)
    total = jogador + computador
    if total % 2 == 0 and parimpar == par:
        print(f'Você ganhou!! O computador jogou {computador} e você jogou {jogador} o total foi {total} e o valor é PAR!')
        vitoria += 1
    elif total % 2 == 0 and parimpar == impar:
        print(f'O computador jogou {computador} e você jogou {jogador} o total foi {total} e o valor é PAR! ')
        print(f'O computador venceu! Seu total de vitórias consecutivas foi de {vitoria}')
        break
    elif total % 2 != 0 and parimpar == impar:
        print(
            f'Você ganhou!! O computador jogou {computador} e você jogou {jogador} o total foi {total} e o valor é ÍMPAR!')
        vitoria += 1
    elif total % 2 != 0 and parimpar == par:
        print(f'O computador venceu! Seu total de vitórias consecutivas foi de {vitoria}')
        print(f'O computador jogou {computador} e você jogou {jogador} o total foi {total} e o valor é ÍMPAR! ')
        break

print('Jogo Finalizado, até breve!')

