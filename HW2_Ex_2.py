#Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.

size = int(input('Введите длину списка - '))
n = 1
my_list = []
for i in range(size):
    n = (1 + 1/n)**n
    my_list.append(n)
summa = 0
for i in range(size):
    summa += my_list[i]
print(my_list)
print(summa)




