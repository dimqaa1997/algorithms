# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

def get_number_letter(language, num):
    if language.lower() == "ru":
        mode = 1071
    elif language.lower() == "en":
        mode = 96
    else:
        raise Exception("алфавит не выбран")

    print(chr(num + mode))


def main():
    get_number_letter(
        language=input("Выберете алфавит\n"
                       "ru - русский\n"
                       "en - английский\n"),
        num=int(input("Введите номер буквы в алфавите: "))
    )


if __name__ == '__main__':
    main()
