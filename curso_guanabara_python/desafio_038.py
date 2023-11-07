# Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))

if n1 > n2:
    print('O PRIMEIRO valor é MAIOR!')
elif n2 > n1:
    print('O SEGUNDO valor é MAIOR')
elif n1 == n2:
    print('Não existe valor maior, os dois valores são IGUAIS')
else:
    print('Insira um valor válido!')