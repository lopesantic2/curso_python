"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato
"""
total = maiormil = cont = menor = 0
maisbarato = ''
print('-=-'*5)
print(' LOJÃO DO WILL ')
print('-=-'*5)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Valor do Produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        maiormil += 1
    if cont == 1 or preco < menor:
        menor = preco
        maisbarato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto na compra foi de R${total}.')
print(f'A quantidade de produtos custando acima de R$1000.00 foi de {maiormil}.')
print(f'O produto mais barato foi a(o) {maisbarato} custando R${menor}')


