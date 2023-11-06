# Você recebe um texto como entrada e deve contar o número de vezes que cada palavra aparece no texto. Para isso, você deve criar um dicionário onde as chaves são as palavras no texto e os valores são o número de vezes que cada palavra aparece. O texto é composto por palavras separadas por espaços e não faz distinção entre maiúsculas e minúsculas. No final, você deve imprimir o dicionário em ordem alfabética das palavras.

# Entrada
# A entrada consiste em várias linhas, sendo que cada linha contém uma sequência de palavras separadas por espaços. A entrada termina quando uma linha contendo somente a palavra FIM é inserida.
#
# Saída
# A saída consiste em linhas, cada uma contendo uma palavra e o número de vezes que ela aparece no texto. As palavras devem ser listadas em ordem alfabética.
#
# Dica
# Você pode usar a função sorted para ordenar as chaves do dicionário. Para isso, passe o dicionário para sorted e use um lambda para especificar que você deseja ordenar pelas chaves. Aqui está como você pode fazer isso:
#
# sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[0]))
#
# Essa linha de código irá ordenar o dicionário word_count alfabeticamente pelas chaves e armazenar o resultado em sorted_word_count. Isso garantirá que as palavras sejam impressas em ordem alfabética.

def contar_palavras(texto):
  """
  Conta o número de vezes que cada palavra aparece em um texto.

  Args:
    texto: O texto a ser analisado.

  Returns:
    Um dicionário onde as chaves são as palavras no texto e os valores são o número de vezes que cada palavra aparece.
  """

  word_count = {}
  for linha in texto.splitlines():
    for palavra in linha.split():
      palavra = palavra.lower()
      if palavra not in word_count:
        word_count[palavra] = 1
      else:
        word_count[palavra] += 1
  return word_count


def main():
  """
  Lê a entrada e imprime a saída.
  """

  texto = input()
  word_count = contar_palavras(texto)
  for palavra, contagem in word_count.items():
    print("{}: {}".format(palavra, contagem))


if __name__ == "__main__":
  main()
