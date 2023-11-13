# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas pessoas já são maiores.

""" pseudocódigo:
1 - ler e informar o ano de nascimento
2 - Criar um input para pessoa informar o ano de nascimento
3 - criar um laço de repetição for para identificar quantos anos as 7 pessoas tem
4 - criar uma condição  para saber se a pessoa é maior de idade
5 - Criei 2 variáveis vazias para acumular a quantidade de pessoas
6 - Criei a funçao if e else para enviar quem for maior para maior e menor para menor
7 - Pedi para imprimir os valores na tela
"""
from datetime import date
data = date.today().year

maior = 0
menor = 0

for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoa}° nasceu? '))
    idade = data - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f'Foi informado {maior} pessoas maiores de idade')
print(f'Foi informado {menor} pessoas menores de idade')