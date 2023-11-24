"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
       num = int(input('Digite um número entre 0 e 20: '))
       if 0 <= num <= 20:
              print(f'Você digitou o número {numeros[num]}.')
       else:
              print('Você digitou um número inválido. Tente novamente.')

# A expressão {numeros[num]} é uma maneira de formatar uma string em Python, conhecida como "f-string" (format string). Ela é usada para incorporar valores de variáveis dentro de uma string. Aqui está uma explicação mais detalhada:
#
# numeros: É a tupla que contém as palavras correspondentes aos números de 0 a 20 em português.
#
# num: É a variável que armazena o número digitado pelo usuário.
#
# {}: Em uma f-string, as chaves {} indicam onde as variáveis devem ser inseridas.
#
# Então, {numeros[num]} significa que o valor da variável num será usado como índice para acessar o elemento correspondente na tupla numeros. Isso é possível porque num é um número inteiro, e os elementos em tuplas são acessados por índices inteiros.
#
# Por exemplo, se o usuário digitar 3, a expressão {numeros[num]} será substituída por numeros[3], o que resulta em 'tres', pois 'tres' é o elemento na posição 3 da tupla numeros. Dessa forma, a string resultante será 'Você digitou o número três.'.