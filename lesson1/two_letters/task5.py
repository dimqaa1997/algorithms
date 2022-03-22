#  Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

def get_two_letters(letter1, letter2, language):
    if language.lower() == "ru":
        mode = 1071
    elif language.lower() == "en":
        mode = 96
    else:
        raise Exception("Некорректный алфавит")
    point_letter1 = ord(letter1) - mode
    point_letter2 = ord(letter2) - mode

    delta_letters = point_letter2 - point_letter1 - 1

    print(f"Позиция первой буквы: {point_letter1}\n"
          f"Позиция второй буквы: {point_letter2}\n"
          f"Букв между ними: {delta_letters}")


def main():
    get_two_letters(
        language=input("Выберете алфавит\n"
                       "ru или en: "),
        letter1=input("Введите первую букву: "),
        letter2=input("Введите вторую букву: ")
    )


if __name__ == "__main__":
    main()
