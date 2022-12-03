#Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
import random
random.randint


size = int(input('Введите длину списка - '))
rnd_list = []
for i in range(size):
    rnd_list.append(random.randint(0, 100))
print(rnd_list)
for i in range(len(rnd_list)):
    if i <= size/2:
        rnd_list.insert(len(rnd_list) - i, rnd_list.pop(i))
print(rnd_list)
