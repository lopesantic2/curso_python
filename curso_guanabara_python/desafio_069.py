"""
Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuario quer ou nao continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados
C) quantas mulheres tem menos de 20 anos
"""
maioridade = 0
homemcad = 0
mulhermenor = 0
while True:
    print('-=-'*15)
    print('CADASTRO DE PESSOAS')
    print('-=-'*15)
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo [M/F]: ')).upper().strip()[0]
    if sexo in 'Mm':
        homemcad += 1
        if idade >= 20:
            maioridade += 1

    if sexo in 'Ff' and idade >= 20:
        maioridade += 1
    if sexo in 'Ff' and idade < 20:
        mulhermenor += 1

    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resposta in 'N':
        print(f'O número de pessoas cadastradas maiores de idade foi de {maioridade}')
        print(f'Foram cadastrados {homemcad} homens.')
        print(f'O total de mulheres cadastradas menores de 20 anos foi de {mulhermenor}')
        break
