# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)

n = int(input('Введите число - '))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(f'Число {n} в двоичной системе равно {b}')