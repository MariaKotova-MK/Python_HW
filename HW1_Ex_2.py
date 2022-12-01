#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            first = not(x or y or z)
            second = (not(x) or not(y) or not(z))
            print(f'{x:^7}{y:^7}{z:^7} --- {first:^7}|{second:^7} --- {(first==second):^7}')