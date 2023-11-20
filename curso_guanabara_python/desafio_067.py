"""
Faça um programa que mostre a tabuada de vários numeros, um de cada vez,
para cada valor digitado pelo usuario. O programa sera interrompido quando o numero for negativo.
"""
tabuada = 0

while True:
    n = int(input('Qual tabuada deseja ver o valor? '))
    sair = str(input('Deseja Sair? [S/N]: ')).strip().upper()[0]

    if n < 0:
        print('O programa foi encerrado. Até breve!!')
        break
    if sair == 'S':
        print('Até Logo!')
        break
    while tabuada < 10:
        tabuada += 1
        m = n * tabuada
        print(f'{n} x {tabuada} = {m}')
    tabuada = 0




