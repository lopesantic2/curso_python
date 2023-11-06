"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

velocidade = int(input('Velocidade em km: '))

vel_limite = 80
multa = (velocidade - vel_limite) * 7

if velocidade > vel_limite:
    print('Você foi multado!')
    print(f'Sua multa foi de R${multa}')

else:
    print('Velocidade permitida!')