# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
import random

size = int(input('Введите размер списка - '))
my_list = [random.randint(0,10) for _ in range(size)]
print(my_list)

if size%2 == 0:
    middle = int(size/2)
else:
    middle = int(size/2 + 1)

new_my_list = []
for i in range(middle):
    new_my_list.append(my_list[i]*my_list[len(my_list) - 1 - i])

print(new_my_list)