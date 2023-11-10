# REFAÇA O DESAFIO_009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO O LAÇO FOR.

num = int(input('Insira o valor que deseja ver a tabuada: '))

for valor in range(1, 10+1):
    m = num * valor
    print(f'{num} X {valor} = {m}')
