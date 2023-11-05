import math

angulo = int(input('Insira o ângulo: '))

cos = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print(f'O cosseno do ângulo de {angulo}° é {cos:.2f}')
print(f'O seno do ângulo de {angulo}° é {seno:.2f}')
print(f'A tangente do ângulo de {angulo}° é {tang:.2f}')