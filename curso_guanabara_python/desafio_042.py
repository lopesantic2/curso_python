# Refaça o desafio_035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

if a < b + c and b < c + a and c < a + b:
    print('Os valores passados PODEM FORMAR um triângulo!', end='')
    if a == b == c:
        print('O seu triângulo é EQUILÁTERO!')
    elif a != b != c != a:
        print('O seu triângulo é ESCALENO!')
    else:
        print('O seu triângulo é ISÓSCELES!')
else:
    print('Os valores passados NÃO PODEM FORMAR um triângulo')