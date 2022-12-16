# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random


size = int(input('Введите размер списка - \n'))
numbers = [random.randint(0, 50) for _ in range(size)] #Добавила list comprehension
new_numbers = []
print(numbers)
for i in range(1, len(numbers), 2):
    new_numbers.append(numbers[i])
print(f'На нечетных позициях элементы {new_numbers} \nИх сумма равна {sum(new_numbers)}')