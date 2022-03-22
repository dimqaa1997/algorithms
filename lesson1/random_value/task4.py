# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random


def get_random_value(start_point, end_point, parse_mode):
    if parse_mode.lower() == "int":
        print(f"Случайное целое число в диапазоне от {start_point} до {end_point} --"
              f" {random.randint(int(start_point), int(end_point))}")

    elif parse_mode.lower() == "float":
        print(f"Случайное вещественное число в диапазоне от {start_point} до {end_point} --"
              f" {random.uniform(int(start_point), int(end_point))}")

    elif parse_mode.lower() == "char":
        char = chr(random.randint(ord(start_point), ord(end_point)))
        print(f"Случайный символ в диапазоне от {start_point} до {end_point} --"
              f" {char}")

    else:
        raise Exception("неверный тип данных")


def main():
    mode = input("Какое значение хотите получить?\n"
                 "int -- целое число\n"
                 "float -- вещественное число\n"
                 "char -- буквенный символ\n"
                 "all -- все и сразу\n")
    if mode == "all":
        start_int = input("Задайте начальную точку диапазона для целых чисел: ")
        end_int = input("Задайте конечную точку диапазона для целых чисел: ")

        start_float = input("Задайте начальную точку диапазона для вещественных чисел: ")
        end_float = input("Задайте конечную точку диапазона для вещественных чисел: ")

        start_char = input("Задайте начальную точку диапазона для буквенных символов: ")
        end_char = input("Задайте конечную точку диапазона для буквенных символов: ")

        get_random_value(start_int, end_int, "int")
        get_random_value(start_float, end_float, "float")
        get_random_value(start_char, end_char, "char")
    else:
        start = input("Задайте начальную точку диапазона: ")
        end = input("Задайте конечную точку диапазона: ")
        get_random_value(start, end, mode)


if __name__ == "__main__":
    main()
