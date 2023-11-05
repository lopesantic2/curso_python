tempo = int(input('Quantos anos tem o seu carro?: '))

# if tempo <= 3:
#     print('Carro novo')
#
# else:
#     print('Carro Velho')

print('carro novo' if tempo <= 3 else 'carro velho') # criar uma condição dessa maneira é somente util se o código for simples e pequeno
print('--FIM--')