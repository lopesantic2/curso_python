# Desenvolva uma lógica que leia o peso e a altura de uma pessoa.
# Calcule seu IMC e mostre seu status de acordo com a tabela:
# - Abaixo de 18.5: ABAIXO DO PESO
# - Entre 18.5 e 25: PESO IDEAL
# - 25 até 30: SOBREPESO
# - 30 até 40: OBESIDADE
# - Acima de 40: OBESIDADE MÓRBIDA

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura ** 2)
print(f'Você tem o peso {peso} e altura {altura} e imc de {imc:.1f}')
if 18.5 <= imc < 25:
    print('Você está ABAIXO DO PESO!')
elif 25 <= imc < 30:
    print('Você está no PESO IDEAL!')
elif 30 <= imc < 40:
    print('Você está OBESO')
else:
    print('Você está com OBESIDADE MÓRBIDA!')
