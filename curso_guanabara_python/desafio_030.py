"""Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar"""

num = int(input('Insira um número: '))

par_impar = num % 2

if par_impar == 0:
    print('O número é par!')

else:
    print('O número é ímpar!')