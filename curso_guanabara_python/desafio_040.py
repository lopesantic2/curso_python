# Crie um programa que leia duas notas de um aluno e calcule sua média. Mostrando uma mensagem no final, de acordo com a media atingida
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('1° nota: '))
nota2 = float(input('2° nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Sua média foi {media:.2f}')
    print('Você foi REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua média foi {media:.2f}')
    print('Você está de RECUPERAÇÃO!')
elif media >= 7.0:
    print(f'Sua média foi {media:.2f}')
    print('PARABÉNS, você foi APROVADO!')