"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
n1 = int(input('Insira o 1° número: '))
n2 = int(input('Insira o 2° número: '))
n3 = int(input('Insira o 3° número: '))

# Verificando qual é o menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n2

# Verificando qual é o maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')