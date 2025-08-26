import random

point_amount = int(input("Anna piste määrä: "))
generated_point_amount = 0
inside_points = 0
points = []


while generated_point_amount < point_amount:
    temp_x_point = random.uniform(-1, 1)
    temp_y_point = random.uniform(-1, 1)
    points.append((temp_x_point, temp_y_point))
    generated_point_amount = generated_point_amount + 1

for x, y in points:
    controller = x**2 + y**2
    if controller < 1:
        inside_points = inside_points + 1

pi = float(4*(inside_points/generated_point_amount))

print(pi)