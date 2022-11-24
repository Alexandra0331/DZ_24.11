# 5. Напишите программу, которая принимает на вход координаты двух точек 
#  и находит расстояние между ними в 2D пространстве.
#  https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
#- 2
# - 1

# out
# 5.099

from math import sqrt
x1 = int(input('Введите значение х  точки A: '))
y1 = int(input('Введите значение y  точки A: '))
x2 = int(input('Введите значение х  точки B: '))
y2 = int(input('Введите значение y  точки B: '))

distance = sqrt(pow(x2-x1,2)+pow(y2-y1,2))
distance = float('{:.3f}'.format(distance))
print(distance)
