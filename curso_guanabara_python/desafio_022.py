"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas
- O nome com todas as letras minusculas
- Quantas letras tem no total (sem considerar espaços)
- Quantas letras tem o primeiro nome"""

nome = input('Insira o seu nome completo: ')

ma_nome = nome.upper()
mi_nome = nome.lower()
tam_nome = len(nome.replace(' ', '')) # replace irá substituir um caractere por outro dependendo do que você colocar, nesse caso eu pedi para que o replace substituisse os espaços em branco, de forma que a frase não tivesse espaço algum entre os caracteres
nnome = nome.split() # Aqui eu dividi o nome em 4 objetos

print(ma_nome)
print(mi_nome)
print(tam_nome)
print(len(nnome[0])) # Nesse print eu pedi para imprimir a variável nnome que foi dividida e que a funçao len, lesse quantos caracteres tem no primeiro bloco da frase
