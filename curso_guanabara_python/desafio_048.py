# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo entre 1 até 500:

soma = 0 # <-- Variável acumuladora
for num in range(1, 501, 2): # Para cada número no intervalo de 1 até 500 pulando de 2 em 2
    if num % 3 == 0: # Se o número for divisível por 3 faça isso:
        soma = soma + num # soma recebe o valor de soma + o valor de num e adiciona esse valor dentro da variável acumuladora SOMA

print(f'A soma dos números ímpares no intervalo de 1 até 500 foi de {soma}')
print('FIM!')
