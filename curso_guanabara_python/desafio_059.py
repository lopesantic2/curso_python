"""Crie um programa que leia dois valores e mostre na tela um menu:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
seu programa deverá realizar a operação solicitava em cada caso"""
from time import sleep

n = int(input('Insira o 1° número: '))
n2 = int(input('Insira o 2° número: '))

soma = 0
multiplicar = 0
while True:
    print('QUAL OPÇÃO VOCÊ DESEJA: \n[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA')
    opcao = int(input('DIGITE A SUA OPÇÃO: '))
    if opcao == 1:
        soma = n + n2
        print(f'A soma dos números resultou em {soma}')
        sleep(2)
    elif opcao == 2:
        multiplicar = n * n2
        print(f'A multiplicação dos números resultou em {multiplicar}')
        sleep(2)
    elif opcao == 3:
        if n > n2:
            print(f'O número {n} é o MAIOR')
            sleep(2)
        else:
            print(f'O número {n2} é o MAIOR')
            sleep(2)
    elif opcao == 4:
        n = int(input('Insira o 1° número: '))
        n2 = int(input('Insira o 2° número: '))
    elif opcao == 5:
        print('FIM')
        break



