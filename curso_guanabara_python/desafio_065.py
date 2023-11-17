"""
Crie um prograam que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

soma = cont = maior = menor = 0
resp = 'S'
while resp in 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    # Calcula o menor e o menor valor
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < maior:
            menor = n
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
# Calcula a média entre a soma e os números inseridos
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
# Mostra o maior e menor valor digitado
print(f'O maior valor que você digitou foi {maior} e o menor foi {menor}')


