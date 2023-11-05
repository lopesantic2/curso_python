"""Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome"""

nome = str(input('Qual o seu nome completo?: ')).strip()

divisao = nome.upper().split()

print('Seu nome tem Silva? {}'.format('SILVA' in divisao))