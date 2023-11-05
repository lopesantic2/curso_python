"""Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes a letra 'A' aparece
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela última vez"""

from unidecode import unidecode # biblioteca que consegue retirar os acentos e símbolos das strings


frase = str(input('Insira uma frase: ')).strip().upper()
frase = unidecode(frase)
qtd_a = frase.count('A')
posicao = frase.find('A')+1
u_posicao = frase.rfind('A')+1

print(f'A letra A apareceu: {qtd_a} vezes na frase')
print(f'Aparece pela primeira vez na posição {posicao}')
print(f'A última letra A apareceu na posição {u_posicao}')