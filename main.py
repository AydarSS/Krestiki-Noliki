gamebox = [['#', '0', '1', 2],
           ['0', '-', '-', '-'],
           ['1', '-', '-', '-'],
           ['2', '-', '-', '-']]
def print_gamebox():
    for i in range(len(gamebox)):
        for j in range(len(gamebox[i])):
            print(gamebox[i][j], end=' ')
        print()

def check_field(x, y):
    if gamebox[x + 1][y + 1] == 'X' or gamebox[x + 1][y + 1] == '0':
        print('Клетка занята, попробуйте снова')
        return False
    return True

def move_in_game(player_num, x, y):
    if player_num % 2 != 0:
        gamebox[x + 1][y + 1] = 'X'
    else:
        gamebox[x + 1][y + 1] = '0'

def check_gorizontal_lines ():

    for i in range(1, 4):
        a = ''
        for j in range(1, 4):
            a = a + gamebox[i][j]
            if a == 'XXX':
                print("Игра закончена. Победили крестики по горизонтали")
                return False
            elif a == '000':
                print("Игра закончена. Победили нолики по горизонтали")
                return False
    return True

def check_vertical_lines ():
    for i in range(1, 4):
        a = ''
        for j in range(1, 4):
            a = a + gamebox[j][i]
            if a == 'XXX':
                print("Игра закончена. Победили крестики по вертикали")
                return False
            elif a == '000':
                print("Игра закончена. Победили нолики по вертикали")
                return False
    return True

def check_diagonal_lines():
    a = ''
    for i in range(1, 4):
        a = a + gamebox[i][i]
        if a == 'XXX':
            print("Игра закончена. Победили крестики по диагонали")
            return False
        elif a == '000':
            print("Игра закончена. Победили нолики по диагонали")
            return False
    b = ''
    for i in range(1, 4):
        b = b + gamebox[i][4-i]
        if b == 'XXX':
            print("Игра закончена. Победили крестики по диагонали")
            return False
        elif b == '000':
            print("Игра закончена. Победили нолики по диагонали")
            return False
    return True

def playing():
    print('Начинаем игру')
    print_gamebox()
    a = True
    num = 1
    while a:
        if num % 2 != 0:
            cordinats = input('Ходят крестики, Введите координаты через пробел: ')
        elif num % 2 == 0:
            cordinats = input('Ходят нолики, Введите координаты через пробел: ')
        if len(cordinats.split()) != 2:
            print("Введите 2 числа")
            continue
        if not(cordinats.split()[0].isdigit()) or not(cordinats.split()[1].isdigit()):
            print("Введите числа")
            continue
        elif (cordinats.split()[0].isdigit() and (int(cordinats.split()[0])<0 or int(cordinats.split()[0])>2)) or (cordinats.split()[0].isdigit() and (int(cordinats.split()[1])<0 or int(cordinats.split()[1])>2)):
            print("Мы пока не настолько опытные, чтобы играть на таком поле, введите числа от 0 до 2")
            continue
        if check_field(int(cordinats.split()[0]), int(cordinats.split()[1])) == False:
            continue
        move_in_game(num, int(cordinats.split()[0]), int(cordinats.split()[1]))
        print_gamebox()
        num += 1
        if check_gorizontal_lines() == False:
            break
        if check_vertical_lines() == False:
            break
        if check_diagonal_lines() == False:
            break
        if num == 10:
            print("Ничья")
            break


playing()