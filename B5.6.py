def salute():
    print('------------------')
    print(' Добро пожаловать ')
    print('      в игру      ')
    print('"Крестики-нолики"')
    print('------------------')
    print('  Правила ввода:  ')
    print('       x y        ')
    print('x - номер строки')
    print('y - номер столбца')
    print('------------------')
    print('   Начнём игру!   ')

def figure():
    print()
    print('   | 0 | 1 | 2 |')
    print('----------------')
    for i, row in enumerate(field):
        row_p = f" {i} | {' | '.join(row)} |"
        print(row_p)
        print('----------------')

def coordinate():
    while True:
        val = input('Введите координаты: ').split()

        if len(val) != 2:
            print('Введите 2 координаты!')
            continue

        x, y = val

        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа!')
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Координаты неверны! Попробуйте ещё раз.')
            continue

        if field[x][y] != " ":
            print('Клетка уже занята!')
            continue

        return x, y

def winner():
    win_combs = [((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                  ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                  ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for comb in win_combs:
        sign = []
        for n in comb:
            sign.append(field[n[0]][n[1]])
        if sign == ['X', 'X', 'X']:
            print('Выиграл крестик! Поздравляем!')
            return True
        if sign == ['O', 'O', 'O']:
            print('Выиграл нолик! Поздравляем!')
            return True

    return False


salute()
field = [[" "] * 3 for i in range(3)]
move = 0
while True:
    move += 1
    figure()

    if move % 2 != 0:
        print('  Ходит крестик  ')
    else:
        print('  Ходит нолик  ')

    x, y = coordinate()

    if move % 2 != 0:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if winner():
        break

    if move == 9:
        print('Вот дела, ничья!')
        break