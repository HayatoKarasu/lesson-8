﻿n = int(input("Введите любое число: "))
sp2 = []

if 1 <= n <= 100000:
    print("Введите", n, "чисел через пробел")
    sp1 = list(map(int, input().split()))
 
    if 1 <= len(sp1) <= 10e9:
        print("Вот ваш список")
        print(sp1)

        sp2.append(sp1[-1])
        sp1.pop(-1)
        sp3 = sp2 + sp1
        
        print("Немного магии!")
        print("Абра Кадабра!")
        print(sp3)
    else:
        print("Неверное количество символов! Пожалуста начните сначала!")
else:
    print("Неверное число! Оно должно быть больше 1 и меньше 100000.")
