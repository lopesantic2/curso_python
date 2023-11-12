# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

"""algoritmo:
1 - digitar a frase, já eliminando os espaços laterais e jogando a frase para maiúsculo.
2 - splitar(separar) em uma nova variável (para que ela gere um vetor (lista)
3 - juntar as palavras  (passo anterior com esse servem para eliminar os espaços internos)
4 - criar uma varíavel vazia, para varrer a string de trás pra frente, gerando a string invertida no laço
5 - criar um laço, retornando o número de caracteres no string, para escrevê-la de trás pra frente,
    começando antes da última letra (- 1), indo até antes da primeira (-1),
    e vai voltando uma letra (-1) #ou simplesmente criar a inversão em uma variável usando fatiamento
6 - declarar o inverso
7 - verificar se o inverso e a junção são iguais com uma condicional simples
"""

frase = str(input('Digite uma frase: ')).strip().upper() #1
palavras = frase.split() #2
juntos = ''.join(palavras) #3
inverso = '' #4
# inverso = juntos[::-1] # FIZ TAMBÉM COM ESSA OPÇÃO QUE EU CONSIDERO MAIS PRÁTICA
for letra in range(len(juntos) - 1, -1, -1): # o -1 depois do len(juntos) vai remover o ultimo 'número' pois a contagem vai sempre de 0 até tal valor, e o len conta de 1 até o valor, fazendo isso temos o resoltado esperado.
    inverso += juntos[letra]
print(f'O inverso de {juntos} é {inverso}')

if inverso == juntos:
    print('É UM PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')
