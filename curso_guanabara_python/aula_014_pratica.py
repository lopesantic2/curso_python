"""
for c in range(1, 10):
    print(c)
print('FIM')
"""
# c = 1
# while c < 10:
#     print(c)
#     c += 1
# print('FIM')]

# QUANDO NÃO SABEMOS O LIMITE DA FUNÇAO, UTILIZAMOS O WHILE
# EX:
# n = 1
# while n != 0: # ENQUANTO N FOR DIFERENTE DE 0, CONTINUE A FUNÇÃO:
#     n = int(input('Digite um valor: '))
# print('FIM')

# r = 'S' # RESPOSTA É IGUAL A "SIM"
# while r == 'S': # ENQUANTO RESPOSTA FOR IGUAL A SIM, CONTINUE APLICANDO A FUNÇÃO:
#     n = int(input('Digite um valor: '))
#     r = str(input('Deseja continuar? [S/N]: ')).upper()
# print('FIM')

n = 1
par = impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
        
print(f'Você digitou {par} números pares e {impar} numeros ímpares!')