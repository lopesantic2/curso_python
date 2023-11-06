"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o VALOR DA CASA, O SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12) # multiplica a quantidade de anos pela quantidade de meses e divide pelo valor da casa, obtendo a prestação.
minimo = salario * 30 / 100  # calcula os 30% minimos do salário que o comprador não pode exceder.

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos ', end='')
print(f'A prestação será de R${prestacao:.2f}')
if prestacao <= minimo: # SE A PRESTAÇÃO FOR MENOR QUE 30% DO SALÁRIO, O EMPRÉSTIMO PODE SER CONCEDIDO.
    print(f'O empréstimo pode ser CONCEDIDO!')
else:
    print('EMPRÉSTIMO NEGADO!')