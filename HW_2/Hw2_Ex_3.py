#Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
import random
random.randint


size = int(input('Введите длину списка - '))
rnd_list = []
for i in range(size):
    rnd_list.append(random.randint(0,100))
print(rnd_list)