"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

reta1 = float(input('Primeiro valor: '))
reta2 = float(input('Segundo valor: '))
reta3 = float(input('Terceiro valor: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os valores passados acima PODEM FORMAR triângulo!')
else:
    print('Os valores passados acima NÃO PODEM FORMAR triângulo!')
