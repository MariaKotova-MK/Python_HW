# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

size = int(input('Введите длину списка чисел Фибоначчи - '))
first_fibo = [1, 0, 1]

for i in range(size):
    first_fibo.append((first_fibo[-2]+first_fibo[-1]))
    first_fibo.insert(0, first_fibo[1] - first_fibo[0])
print(first_fibo)