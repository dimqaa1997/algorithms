# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def get_sum_and_prod(num):
    num1 = num % 10
    num2 = (num // 10) % 10
    num3 = (num // 100) % 10

    sum_num = num1 + num2 + num3
    prod_num = num1 * num2 * num3

    return sum_num, prod_num


def main():
    sum_num, prod_num = get_sum_and_prod(int(input("Введите трехзначное число: ")))
    print(f"Сумма = {sum_num}\n"
          f"Произведение = {prod_num}")


if __name__ == '__main__':
    main()
