# Elabore um programa que calcule o valor a ser pago
# por um produto, considerando seu PREÇO NORMAL e
# CONDIÇÃO DE PAGAMENTO:
# - À vista DINHEIRO / CHEQUE: 10% DSCT
# - À vista no CARTÃO: 5% DSCT
# - Em 2x no CARTÃO: preço normal
# - 3x ou mais no CARTÃO: 20% de juros

compra = float(input('Qual o valor da compra? R$'))

print(
    'Qual a forma de pagamento desejada? \n[1] À VISTA DINHEIRO/CHEQUE \n[2] À VISTA NO CARTÃO \n[3] 2x NO CARTÃO \n[4] 3x OU MAIS NO CARTÃO')

opcao = int(input('Insira a opção desejada: '))

if opcao == 1:
    total = compra - (compra * 10 / 100)
    print(f'O valor da sua compra com desconto à vista é de {total:.2f}')

elif opcao == 2:
    total = compra - (compra * 5 / 100)
    print(f'O valor da sua compra com desconto à vista no cartão é de {total:.2f}')

elif opcao == 3:
    parcela = compra / 2
    print(f'Sua compra de R${compra:.2f} será parcelada em 2x de R${parcela}')

elif opcao == 4:
    total = compra + (compra * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    total = compra
    print('OPÇÃO INVÁLIDA DE PAGAMENTO')
print(f'Sua compra de R${compra:.2f} vai custar R${total:.2f} no final')


