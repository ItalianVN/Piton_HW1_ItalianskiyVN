# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти от 1 до 4, для того чтобы узнать диапазон возможных координат: '))

if a == 1:
    print('В первой четверти возможный диапазон координат - x > 0, y > 0')
elif a == 2:
    print('Во второй четверти возможный диапазон координат - x < 0, y > 0')
elif a == 3:
    print('В третьей четверти возможный диапазон координат - x < 0, y < 0')
elif a == 4:
    print('В четвертой четверти возможный диапазон координат - x > 0, y < 0')
else:
    print('Заданной четверти нет')