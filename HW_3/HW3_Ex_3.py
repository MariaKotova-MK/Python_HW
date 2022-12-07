# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

size = int(input('Введите размер списка - '))
my_list = [round(random.uniform(0,10), 3) for _ in range(size)]
print(my_list)

fraction = list(map(lambda x: x - int(x), my_list))
fraction = list(map(lambda x: round(x, 3), fraction))

difference = round(max(fraction) - min(fraction), 3)
print(f'Разница между максимальной и минимальной дробной часть. элементов равна {difference}')