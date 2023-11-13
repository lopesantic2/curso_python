"""
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valroes 'M' ou 'F'.
    Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = 'MF'
while sexo not in 'M' and sexo not in 'F':
    sexo = str(input('Insira o sexo: [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        print('Sexo masculino cadastrado com sucesso!')
    if sexo == 'F':
        print('Sexo feminino cadastrado com sucesso!')
    if sexo != 'MF':
        print('Dados Inválidos! Insira novamente')

# CORREÇÃO ##

# sexo = str(input('Insira o sexo: [M/F]: ')).strip().upper()[0]
#
# while sexo not in 'MF':
#     sexo = str(input('Dados inválidos, por favor, digite seu sexo: '))
# print(f'Sexo {sexo} cadastrado com sucesso!')