"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
"""

num = int(input('Insira um número qualquer: '))

escolha = int(input('[1]Binário \n[2]Octal \n[3]Hexadecimal \nEscolha uma das opções de conversão:  '))


if escolha == 1:
    binario = bin(num)[2:]
    print(f'O número {num} transformado em binário é: {binario}')
elif escolha == 2:
    octal = oct(num)[2:]
    print(f'O número {num} em base Octal é: {octal}')
elif escolha == 3:
    hexa = hex(num)[2:]
    print(f'O número {num} convertido para hexadecimal é: {hexa}')
else:
    print('OPÇÃO INVÁLIDA!')