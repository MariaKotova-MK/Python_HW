# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера.
# Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""
import random

print('Начнем игру. Правила простые - на столе 150 конфет. За один раз можно максимум 28 конфет\nПобедит тот, кто сделает последний ход!\n')


while True:
    a = int(input('Cейчас мы жеребьевкой определим кто будет ходить первым. Введите число от 1-10 - '))
    if 0 <= a <= 10:
        b = random.randint(1, 10)
        print(f'Число компьютера {b}')
        if a > b:
            print('Вы ходите первым')
            current_gamer = 1
        else:
            print('Компьютер ходит первым\n')
            current_gamer = 2
        break
    else:
        print('введите корректное число')

count = 150
max = 28
while count > 0:
    print(f'количество оставшихся конфет: {count}\n')
    if current_gamer == 1:
        while True:
            number_to_delete = int(input('Ваш ход: - '))
            if number_to_delete >= 1 and number_to_delete <= 29:
                break
        current_gamer = 2
    else:
        if count <= 29:
            number_to_delete = count
        else:
            number_to_delete = random.randint(1, 29)
        print(f'Ход компьютера - {number_to_delete}')
        current_gamer = 1
    count -= number_to_delete


if current_gamer == 2:
    print('Вы победили!Ура!')
else:
    print('Вы проиграли. Не расстраивайтесь, попробуйте ещё раз')


