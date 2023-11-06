"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
"""
from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual '))

if ano == 0:
    ano = date.today().year
print(f'Bem Vindo ao ano de {ano}!')

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto!')

else:
    print(f'O ano de {ano} não é bissexto!')


