##TODU FOR EM PYTHON É UM "FOR EACH"

# percorrer uma lista

# lista_produtos = ['faca', 'garfo', 'panela', 'frigideira', 'flavorstone']
#
# for produto in lista_produtos: # PARA CADA PRODUTO DENTRO DA LISTA DE PRODUTOS
#     print(produto.capitalize()) # IMPRIMA OS PRODUTOS CAPITALIZANDO ELES

"""
O nome que você dá para o for tanto faz, ele servirá somente para deixar o código
intuitivo. Use sempre nomes intuitivos para ficar mais fácil a visualização.

"""

# CALCULAR O IMPOSTO SOBRE VÁRIOS VALORES

# lista_precos = [10, 10, 200, 50, 300]
# for preco in lista_precos:
#     imposto = preco * 0.1
#     print(imposto)

# PERCORRENDO UM DICIONÁRIO

# produtos = {
#     'faca': 10,
#     'garfo': 10,
#     'panela': 200,
#     'frigideira': 50,
#     'flavorstone': 300,
# }
#
# for produto in produtos:
#     print(produtos)
#     print(produtos[produto])

## RANGE ##
#
# for i in range(5):
#     print('will')
#
with open('vendasloja.txt', 'r') as arquivo: # abre o arquivo .txt
    texto = arquivo.read()
lista_texto = texto.split('\n')
faturamento = 0

# excluir a 1° linha
lista_texto = lista_texto[1:]  # <-- o [1:] está dizendo "ignore o primeiro item e percorra até o final"

# para cada linha do meu arquivo
for linha in lista_texto:  # para cada linha na lista
    posicao_pv = linha.find(";")  # encontre o ;
    valor = float(linha[posicao_pv+1:])  # quero pegar o valor depois do indice do ";" e somar mais 1
    faturamento += valor
print(f'R${faturamento}')


