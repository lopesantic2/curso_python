# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética.
# No final, mostre os 10 primeiros termos dessa progressão:

primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") ) # Razão é de quanto em quanto queremos pular

ultimo = primeiro + (10-1) * razao

for var in range(primeiro, ultimo+1, razao):
    print(f'{var}', end=' -> ')
print('ACABOU')