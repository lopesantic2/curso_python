"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'"""

cidade = str(input('Em que cidade você nasceu: ')).strip() # # ele irá remover os espaços no inicio e no final da string

print(cidade[0:5].upper() == 'SANTO') # .upper() - Tudo que estiver em minusculo ou misturado, ele íra deixar em maiusculo