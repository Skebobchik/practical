def check_triangle():
    print("Введите длины сторон треугольника:")

    try:
        side1 = int(input("Сторона A >>> "))
        side2 = int(input("Сторона B >>> "))
        side3 = int(input("Сторона C >>> "))
    except ValueError:
        print("Ошибка: нужно вводить целые числа!")
        return

    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        print("Ошибка: Треугольник с такими сторонами не существует!")
        return

    if side1 == side2 == side3:
        print("Полученный треугольник: равносторонний")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Полученный треугольник: равнобедренный")
    else:
        print("Полученный треугольник: разносторонний")


if __name__ == "__main__":
    check_triangle()
