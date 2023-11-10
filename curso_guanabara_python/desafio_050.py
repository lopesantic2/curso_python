# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se
# o valor digitado for ímpar, desconsidere-o:

soma = 0

for n in range(1, 7):
    num = int(input(f'Insira o {n}° valor: '))
    if num % 2 == 0:
        soma += num
print(f"A soma de todos os valores pares foi de {soma}")
