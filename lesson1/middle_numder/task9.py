# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def get_middle_number(num1, num2, num3):
    if num1 < num2 < num3:
        middle = num2
    elif num2 < num1 < num3:
        middle = num1
    elif num1 < num3 < num2:
        middle = num3
    else:
        middle = "отсутствует"

    print(f"Среднее число {middle}")


def main():
    get_middle_number(
        int(input("Введите первое число: ")),
        int(input("Введите второе число: ")),
        int(input("Введите третье число: "))
    )


if __name__ == "__main__":
    main()
