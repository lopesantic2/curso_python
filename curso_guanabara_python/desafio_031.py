"""
Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas
"""

distancia = int(input('Qual a distância em Km da sua viagem?: '))


if distancia <= 200:
    valor = distancia * 0.50
    print(f'Sua viagem terá {distancia}Km e o valor que você irá pagar é de R${valor} ')

elif distancia > 200:
    valor = distancia * 0.45
    print(f'Sua viagem terá {distancia}Km e o valor que você irá pagar é de R${valor}')

else:
    print('Digite um valor válido!')