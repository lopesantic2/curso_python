
# Tuplas

# AS TUPLAS SÃO IMUTÁVEIS !!!!!!

# Em programação, uma tupla é uma coleção de dados ordenada e finita. É semelhante a uma lista, mas é imutável, o que significa que não pode ser alterada após sua criação. As tuplas são frequentemente usadas para armazenar dados que precisam ser mantidos em uma ordem específica, como as coordenadas de um ponto ou o nome e a idade de uma pessoa.
#
# Uma tupla pode conter qualquer tipo de dado, incluindo números, strings, listas, tuplas, etc. Os elementos de uma tupla são separados por vírgulas e podem ser encerrados em parênteses ou não. Por exemplo, as seguintes são todas tuplas válidas:
# Tupla sem parênteses

# tupla = 1, 2, 3

# Tupla com parênteses
# tupla = (1, 2, 3)

# Tupla com elementos de diferentes tipos
# tupla = 'a', 1, [1, 2, 3]

# Para acessar um elemento de uma tupla, podemos usar sua posição. Por exemplo, para acessar o primeiro elemento da tupla tupla, podemos usar a seguinte sintaxe:

# print(tupla[0])

# Isso imprimirá o valor 1.
# Podemos também usar um loop para iterar sobre os elementos de uma tupla. Por exemplo, o seguinte código imprimirá cada elemento da tupla tupla:
#
# for elemento in tupla:
#     print(elemento)

# Isso imprimirá o seguinte:
# 1
# 2
# 3
# As tuplas são uma ferramenta útil para armazenar e manipular dados. Elas são frequentemente usadas em programação para representar dados que precisam ser mantidos em uma ordem específica.

#             0          1        2        3
lanche = 'hamburguer', 'suco', 'pizza', 'pudim'

print(lanche[2])
print(lanche[0:2]) # 0:2 significa vai do 1° item até o 3°
print(lanche[1:]) # 1: significa "comece no 1 e vai até o final"
print(lanche[-1]) # -1 imprime o ultimo elemento
print(len(lanche))

for comida in lanche: # irá criar uma variavel simples
    print(comida)
    