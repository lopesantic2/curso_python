                         ### FATIAMENTO DE STRING ###

frase = 'Curso em Vídeo Python'
# frase = '   Aprenda Python   '

# print(frase[9:21:2]) # nesse fatiamento ele vai de 9 até 21 pulando de 2 em 2 caracteres
#
# print(frase[:5]) # nesse fatiamento, ele vai de 0 até a letra 5
#
# print(frase[15:]) # indica o inicio, mas não indica o final, no caso ele iria do caractere 15 até o final
#
# print(frase[9::3]) # significa que ele irá de do caractere 9 até o final, pulando de 3 em 3 caracteres

                         ### ANALISE DE STRING ###

# tam_frase = len(frase)
# contador_frase1 = frase.count('o')
# contador_frase2 = frase.count('o', 0, 13)
# encontre_frase = frase.find('deo')
# encontre_frase_teste = frase.find('Android') # quando não existir dentro da frase, irá retornar o valor -1 que significa que n foi encontrado
# verdadeiro_falso_frase = 'curso' not in frase
#
# print(tam_frase)
# print(contador_frase1)
# print(contador_frase2)
# print(encontre_frase)
# print(encontre_frase_teste)
# print(verdadeiro_falso_frase)


                         #### TRANSFORMAR STRING####

# substituir_frase = frase.replace('python', 'Android') # Substitui o que tinha por algo novo
# maiusculo_frase = frase.upper() # Tudo que estiver em minusculo, ele íra deixar em maiusculo
# minusculo_frase = frase.lower() # Tudo que estiver em maiusculo, ele ira deixar em minusculo
# capitalizar_frase = frase.capitalize() # Vai deixar a primeira letra da frase como maiusculo e toda frase restante em minusculo
# titulo_frase = frase.title() # Analisa qual o tamanho da frase, transformando cada inicio de palavra como maiusculo e o restante dela como minusculo
#
# remover_espaco_frase = frase.strip() # ele irá remover os espaços inuteis no inicio e no final da string, dentro do strip, temos tambem o frase.rstrip() - que remover somente os espaços da direito e o frase.lstrip() - que irá remover somente os espaços da esquerda
#
#
# print(substituir_frase)
# print(maiusculo_frase)
# print(minusculo_frase)
# print(capitalizar_frase)
# print(titulo_frase)
# print(remover_espaco_frase)

                         ### DIVISÃO DE STRING ###

# divide_espaco_frase = frase.split() # PEGA OS ESPAÇOS EM BRANCO DA STRING E DIVIDE EM BLOCOS (REFAZ OS ÍNDICES QUANDO DIVIDIE, GERANDO LISTAS DO 0 SEMPRE QUE TIVER ESPAÇOS EM BRANCO NA FRASE)
#
# print(divide_espaco_frase)
#
#                          ### JUNÇAO DE STRING ###
#
# juntar_na_frase = '-'.join(frase) # Ele irá juntar todos os elementos de frase e irá usar o separador nos espaços vazios
# print(juntar_na_frase)