# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

import math

a_x_coord = int(input("Введите X точки A: "))
a_y_coord = int(input("Введите Y точки A: "))
b_x_coord = int(input("Введите X точки B: "))
b_y_coord = int(input("Введите Y точки B: "))
result = math.sqrt (((b_x_coord-a_x_coord) ** 2) + ((b_y_coord-a_y_coord) ** 2))
result = round (result, 2)
print(f"Расстояние между точкой A ({a_x_coord},{a_y_coord}) и точкой B ({b_x_coord},{b_y_coord}) = {result}")

