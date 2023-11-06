"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Insira o salário do seu funcionário: R$'))

if salario > 1250:
    novo_salario = (salario * 0.10) + salario
    print(f'O valor do salário de R${salario:.2f} passará a ser de R${novo_salario:.2f}')
elif salario <= 1250:
    novo_salario = (salario * 0.15) + salario
    print(f'O valor do salário de R${salario:.2f} passará a ser de R${novo_salario:.2f}')
else:
    print('Insira um valor válido!')