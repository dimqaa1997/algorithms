# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

def get_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print("Это високосный год")
    elif year % 400 == 0 and year % 100 == 0:
        print("Это високосный год")
    else:
        print("Год невисокосный")


def main():
    get_leap_year(int(input("Введите интересующий Вас год: ")))


if __name__ == "__main__":
    main()
