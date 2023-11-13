"""
Refaça o desafio_051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
utilizando a estrutura while
"""

primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") ) # Razão é de quanto em quanto queremos pular

termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')
