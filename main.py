import matplotlib.pyplot as plt
from Point_1 import Point_1
import math


# Основна функція
def main():
    # пустий масив точок
    points = []
    # Вводимо координати точок
    # та створюємо екземпляри класу Point_1
    print("Enter X,Y values for 3 points:")
    for i in range(3):
        try:
            tmp_x = float(input("X{}: ".format(i+1)))
            tmp_y = float(input("Y{}: ".format(i + 1)))
        except ValueError:
            print("Wrong values for points!")
            exit()
        else:
            tmp_point = Point_1(tmp_x, tmp_y)
            print(Point_1.get_count())
            points.append(tmp_point)
    # Відображення точок до змін
    show_points(points)
    # Обробка точок за варіантом
    task1(points)
    # Відображення точок після змін
    show_points(points)
    # Збереження координат точок у файлі
    save_points(points)


# Функція для обробки точок за варіантом
def task1(list_of3_points):
    """Створити список з трьох точок, порахувати відстань між першою і
    третьою, пересунути другу на 6 вліво."""
    point_1 = list_of3_points[0]
    point_2 = list_of3_points[1]
    point_3 = list_of3_points[2]
    length = math.sqrt(math.pow(point_3.get_x() - point_1.get_x(), 2) + math.pow(point_3.get_y() - point_1.get_y(), 2))
    point_2.shift(-6.0, 0.0)
    print("Length = {}".format(length))


# відображення графічних об'єктів
def show_points(list_of_points):
    # work with plot
    x = [point.get_x() for point in list_of_points]
    y = [point.get_y() for point in list_of_points]
    plt.plot(x, y, 'ro')
    plt.grid()
    plt.show()


# збереження координат у файлу
def save_points(list_of_points):
    with open("output.txt", "w") as f:
        for num, point in enumerate(list_of_points):  # 0: point1, 1: point2, 2: point3
            #f.write(f"{num+1}: {point.get_x()}; {point.get_y()}\n")
            f.write(f"({num+1}) {point.get_x()}:{point.get_y()}\n")


if __name__ == '__main__':
    main()
