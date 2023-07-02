def greet():
    print("---------------------")
    print("Игра крестики-нолики!")
    print("---------------------")
    print("  формат ввода: x y  ")
    print("  x - номер строки   ")
    print("  y - номер столбца  ")
    print("---------------------")


def show_field():
    print()
    print(f"  | 0 | 1 | 2 |")
    print("---------------")
    for i, row in enumerate(field):
        row_str = " | ".join(row)
        print(f"{i} | {row_str} |")
        print("---------------")
    print()


def ask_coordinates():
    while True:
        coordinates = input("Ваш ход: ").split()

        if len(coordinates) != 2:
            print("Введите 2 координаты через пробел!")
            continue

        x, y = coordinates

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты вне диапазона!")
            continue

        if field[x][y] != " ":
            print("Клетка занята, введите другие координаты")
            continue

        return x, y


def check_win():
    win_coordinates = (
        ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))
    )

    for cord in win_coordinates:
        symbols = []

        for c in cord:
            symbols.append(field[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            print("Выиграл крестик!")
            return True

        if symbols == ["0", "0", "0"]:
            print("Выиграл нолик!")
            return True
    return False


greet()
field = [[" ", " ", " "] for i in range(3)]
count = 0
while True:
    count += 1
    show_field()

    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask_coordinates()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        show_field()
        print("Ничья!")
        break
