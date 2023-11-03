"""
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

km_percorrido = float(input('km percorrido: '))
qtd_dias = int(input('Dias alugados: '))

# km = km_percorrido * 1000

preco_km = km_percorrido * 0.15
preco_dia = qtd_dias * 60

preco = preco_dia + preco_km

print(f'O valor por km é de: R${preco_km} \nO valor pelo dia é de: R${preco_dia} \nO valor total do aluguel é de: R${preco}')