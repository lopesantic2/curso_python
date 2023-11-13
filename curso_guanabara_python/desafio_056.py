# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo, Qual é o nome do homem mais velho, quantas mulheres tem menos de 20 anos.


soma_idade = 0
mediaidade = 0
maioridadehomem = 0
maisvelho = ''
totalmulher20 = 0
for p in range(1, 5): 
    print(f'{p}° PESSOA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1


mediaidade = soma_idade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {maisvelho}')
print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anos')