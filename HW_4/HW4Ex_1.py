# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите максимальную степень в многочлена - '))

def create_eq(k):
    coeff = {}
    for i in range(k+1):
        coeff[i] = random.randint(0,100)
    print(coeff)

    equation = ''
    for i in range(k, -1, -1):
        if coeff[i] != 0:
            if coeff[i] == 1:
                if i == 1:
                    equation += f'x + '
                elif i == 0:
                    equation += f'1 + '
                else:
                    equation += f'x**{i} + '
            else:
                if i == 1:
                    equation += f'{coeff[i]}*x + '
                elif i == 0:
                    equation += f'{coeff[i]}'
                else:
                    equation += f'{coeff[i]}*x**{i} + '
    return equation + '= 0'

print(create_eq(k))

