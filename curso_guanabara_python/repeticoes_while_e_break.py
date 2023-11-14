"""
Repetições
While(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando o código não tem fim
### MUITO CUIDADO COM O METÓDO *CONTINUE* POIS ELE PODE QUEBRAR SEU CÓDIGO E REPETIR INFINITAMENTE
"""
# EX LOOP INFINITO
"""
condicao = True
while condicao:
    nome = input('Qual o seu nome? ')
    print(f'O seu nome é {nome}')
    if nome == sair:
        break # IRÁ TERMINAR O CÓDIGO SEMPRE QUE ENCONTRAR BREAK
print('FIM')
"""
# COMO FAZER O CONTADOR CONTAR ATÉ DETERMINADO NÚMERO COM WHILE

"""contador = 0
while contador < 10 + 1: # Enquanto o contador for menor do que 10
    print(contador) # imprime o valor do contador
    contador += 1 # soma o valor antigo do contador com 1 (se contador == 0 irá fazer 0+1 e assim em diante)
print('FIM')
"""

# WHILE + CONTINUE
"""contador = 0
while contador <= 100:
    contador += 1

    # PODEMOS TER VÁRIOS CONTINUE, QUANDO A CONDIÇÃO DELE FOR VERDADEIRA, ELE VOLTA NO COMEÇO DO LAÇO
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    # ESSA CONDIÇÃO TERMINA O LAÇO
    if contador == 40:
        break

print('Acabou')"""


## WHILE + WHILE

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas: # Esse while irá rodar 5x a cada execução do 1° while
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('ACABOU')