"""
Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando
o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados
e qual foi a soma entre eles (desconsiderando a flag)
"""
n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Foram digitados {cont} números e a soma deles resultou em {soma:.2f}')
