# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите число X не равное нулю:'))
y = int(input('Введите число Y не равное нулю:'))


if x == 0 and y == 0:
    print('Условия ввода координат выполнены неверно')
elif x > 0 and y > 0:
    print(f'Точка с координатами x = {x} и y = {y} находится в 1 четверти')
elif x < 0 and y > 0:
    print(f'Точка с координатами x = {x} и y = {y} находится во 2 четверти')
elif x < 0 and y < 0:
    print(f'Точка с координатами x = {x} и y = {y} находится в 3 четверти')
elif x > 0 and y < 0:
    print(f'Точка с координатами x = {x} и y = {y} находится в 4 четверти')