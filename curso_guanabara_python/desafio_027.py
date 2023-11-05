"""
Faça um pprograma que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
EX:
Ana Maria de Souza
primeiro = Ana
ultimo = Souza
"""

nome = str(input('Insira o seu nome completo: ')).strip()
lista = nome.split()

print(f'Olá {nome}!')
print(f'O seu primeiro nome é {lista[0]}')
print(f'O seu último nome é {lista[-1]}')
print(f'O seu último nome é {lista[len(lista)-1]}')