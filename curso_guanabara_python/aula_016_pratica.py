lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') # Tupla pode ser feita sem os parenteses no python 3
# !!!!!!! TUPLAS SÃO IMUTÁVEIS !!!!!!!

# print(lanche[::2])
# print(len(lanche))
#
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}')
# #
#
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')