#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

x1 = int(input('Введите значение x первой точки- '))
y1 = int(input('Введите значение y первой точки- '))
x2 = int(input('Введите значение x второй точки- '))
y2 = int(input('Введите значение y второй точки- '))
distance = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))**0.5
print(distance)
