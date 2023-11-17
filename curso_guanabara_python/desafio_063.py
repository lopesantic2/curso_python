"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma sequencia de fibonacci
ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""
print('-=' * 11)
print('Sequência de Fibonacci')
print('-=' * 11)

n = int(input('Insira o termo desejado: '))
f1 = 0
f2 = 1
f3 = 0
cont = 3
print(f'{f1}->{f2}', end='->')
while cont <= n:
    f3 = f1 + f2
    print(f'{f3}', end='->')
    f1 = f2
    f2 = f3
    cont += 1
print('Fim')
