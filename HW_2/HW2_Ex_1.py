#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = int(input('Введите целое число: '))
suma = 0

while number > 0:
    digit = number % 10
    suma = suma + digit
    number = number // 10

print(f'Сумма цифр равна {suma}')