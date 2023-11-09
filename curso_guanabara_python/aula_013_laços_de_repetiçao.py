# for c in range(0, 6):
#     print('Oi')
# print('FIM')
#
# for b in range(1, 7):
#     print(b)
# print('FIM')
#
# for d in range(6, 0, -1):
#     print(d)
# print('FIM')

# n = int(input('Digite um número: '))
# for c in range(0, n+1): # O mais um vai fazer com que o python não ignore o ultímo número
#     print(c)
# print('FIM')

# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
#
# for c in range(i, f+1, p):
#     print(c)
# print('FIM')

s = 0 # S recebe o valor de 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n # soma o valor da váriavel 0 e soma com o valor de n
print(f'O somatório de todos os valores foi {s}') # imprime a soma de todos os valores de n que foram adicionados na variável s