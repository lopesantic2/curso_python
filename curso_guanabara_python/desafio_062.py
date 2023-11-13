"""
Melhore o desafio_061 perguntando ao usuario se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser que quer mostrar 0 termos.
"""

primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") ) # Razão é de quanto em quanto queremos pular

termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
