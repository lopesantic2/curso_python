import random

a1 = input('Insira o nome do 1° aluno: ')
a2 = input('Insira o nome do 2° aluno: ')
a3 = input('Insira o nome do 3° aluno: ')
a4 = input('Insira o nome do 4° aluno: ')

lista = [a1, a2, a3, a4]

sorteado = random.choice(lista)

print(f'O aluno sorteado foi {sorteado}')
