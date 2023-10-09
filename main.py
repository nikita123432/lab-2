def create_chessboard(n, m):
    chessboard = []

    try:
        for i in range(n):
            row = []
            for j in range(m):
                cell_value = int(input(f"Введите значение для элемента ({i}, {j}): "))
                row.append(cell_value)

            chessboard.append(row)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        return chessboard


try:
    n = int(input("Введите количество строк (n): "))
    m = int(input("Введите количество столбцов (m): "))
except ValueError:
    print("Ошибка ввода: введите целые числа.")
else:
    chessboard = create_chessboard(n, m)

for row in chessboard:
    print(row)

zero = 0

for j in range(m):
    zero = False
    for i in range(n):
        if chessboard[i][j] == 0:
            is_non_zero_column = True
            break
    if not is_non_zero_column:
        zero += 1


# Выведите информацию о не нулевых столбцах и их количество
if zero > 0:
    print(f"Количество столбцов, не содержащих ни одного нулевого элемента: {zero}")

else:
    print("Все столбцы нулевые.")