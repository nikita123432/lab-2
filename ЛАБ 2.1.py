def is_prime():
    try:
        i = int(input())
    except ValueError:
        return"Вы ввели не число"
    if 0 < i <= 1000:
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            if i == 2 or i == 3 or i == 5 or i == 7:
                return False

            return True
        else:
            return False


    else:
        print("ОТ 0 ДО 1000")


print(" Результат ", is_prime())