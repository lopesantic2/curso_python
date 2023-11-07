# A Federação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# - até 9 anos: MIRIM
# - até 14 anos: INFANTIL
# - até 19 anos: JUNIOR
# - até 25 anos: SÊNIOR
# - acima: MASTER

from datetime import date
ano_atual = date.today().year

ano_nasc = int(input('Qual o ano do seu nascimento? '))

idade = ano_atual - ano_nasc
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')

elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')

elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')

elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')

else:
    print('Classificação: MASTER')