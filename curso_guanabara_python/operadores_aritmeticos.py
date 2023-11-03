"""
    + = soma
    - = subtração
    * = multiplicação
    / = divisão
    ** = potência
    // = divisão inteira
    % =  resto da divisão

    ORDEM DE PRECEDÊNCIA
    1° = () - se tem parentêses, ele será executado primeiro
    2° = potência
    3° = *, /, //, % - irá aparecer o que vier primeiro!
    4° = +, -

"""

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2

print(f'A soma é {s} \nA multiplicação é {m} \nA divisão é {d:.2f}')
print(f'\nA divisão inteira é {di} \nA potência é {e} \nO resto é {r}')
