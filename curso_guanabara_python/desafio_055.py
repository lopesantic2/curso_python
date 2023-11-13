# faça um programa que leia o peso de cinco pessoas. No final, mostra qual foi o maior e o menor peso lido

""" PSEUDCÓDIGO
"""

lst=[]  #lista vazia
for c in range(1, 6):
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    lst+=[peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lst))  #maximo valor da lista
print('O Menor peso foi:', min(lst) )  #minimo valor da lista