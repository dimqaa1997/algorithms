# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
def get_func(x1, y1, x2, y2):
    A = y1 - y2
    B = x2 - x1
    C = x1 * y2 - x2 * y1

    if not A:
        print(f"f(x) = {B}y + {C}")
    elif not B:
        print(f"f(x) = {A}x + {C}")
    elif not (A and B):
        print("Точки должны быть разными")
    else:
        print(f"f(x) = {A}x + {B}y + {C}")


def main():
    get_func(float(input("Введите начальную координату по оси X: ")),
             float(input("Введите начальную координату по оси Y: ")),
             float(input("Введите конечную координату по оси X: ")),
             float(input("Введите конечную координату по оси Y: ")))


if __name__ == "__main__":
    main()
