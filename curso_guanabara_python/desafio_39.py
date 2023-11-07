# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade, se ele ainda vai se alistar ao serviço militar ou se é a hora de se alistar ou se já passou o tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# FEITO PARA IDADE #
# idade = int(input('Qual sua idade? '))
#
# tempo_alistar = 18 - idade
# passou_alistar = idade - 18
#
#
# if idade < 18:
#     print('Você ainda vai se alistar!')
#     if tempo_alistar == 1:
#         print(f'Ainda falta {tempo_alistar} ano para você se alistar!')
#     elif tempo_alistar > 1:
#         print(f'Ainda falta {tempo_alistar} anos para você se alistar!')
#
# elif idade == 18:
#     print('Já está na hora de você se alistar')
# elif idade > 18:
#     print('Já passou do tempo do alistamento!')
#     if passou_alistar == 1:
#         print(f'Você está {passou_alistar} ano atrasado do tempo de alistamento!')
#     elif passou_alistar > 1:
#         print(f'Você está {passou_alistar} anos atrasado do tempo de alistamento!')

# COM O ANO DE NASCIMENTO
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {atual}')
if idade == 18:
    print(f'Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')

elif idade> 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')