from math import hypot

co = float(input('Insira o cateto oposto: '))
ca = float(input('Insira o cateto adjacente: '))

h = hypot(co, ca)

print(f'A soma do cateto oposto {co} e o cateto adjacente {ca} tem como resulltado \na hipotenusa {h:.2f}')