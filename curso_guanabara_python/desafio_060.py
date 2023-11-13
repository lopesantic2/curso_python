"""
Faça um programa que leia um número qualquer e mostre o seu fatorial:
EX: 5! = 5x4x3x2x1 = 120
"""
# JEITO DE SE FAZER COM BIBLIOTECA #
    # from math import factorial
    # n = int(input('Digite um número para calcular seu fatorial: '))
    # f = factorial(n)
    # print(f'O fatorial de {n} é {f}')


n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'CALCULANDO {n}! ')
while c > 0:
    print(f'{c}', end= '')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

