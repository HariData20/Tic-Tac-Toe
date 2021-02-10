# write your code here
import sys


def who_wins(c_x, c_o):
    if c_x == 3:
        print('X wins')
        sys.exit()
    elif c_o == 3:
        print('O wins')
        sys.exit()
    else:
        return 1


def print_tic_tac_toe(x):
    cells = x

    print('---------')
    print(f'| {cells[0]} {cells[1]} {cells[2]} |')
    print(f'| {cells[3]} {cells[4]} {cells[5]} |')
    print(f'| {cells[6]} {cells[7]} {cells[8]} |')
    print('---------')


x = '         '
list1 = []
print_tic_tac_toe(x)
who_is_next = 1
while True:
    list1 = []
    print('Enter the coordinates:')
    x_cor, y_cor = input().split()
    if not x_cor.isdigit() or not y_cor.isdigit():
        print('You should enter numbers!')
        continue
    if int(x_cor) >= 4 or int(y_cor) >= 4 or int(x_cor) < 1 or int(y_cor) < 1:
        print('Coordinates should be from 1 to 3!')
        continue
# insert into string
    index = (int(x_cor) - 1) + ((3 - int(y_cor)) * 3)
    if x[index] in ('X','O'):
        print('This cell is occupied! Choose another one!')
        continue
    if x[index] == ' ':
        if who_is_next == 1 or who_is_next % 2 == 1:
            x = x[:index]+'X'+x[index + 1:]
            who_is_next += 1
            print_tic_tac_toe(x)
        elif who_is_next % 2 == 0:
            x = x[:index] + 'O' + x[index + 1:]
            who_is_next += 1
            print_tic_tac_toe(x)
    if who_is_next > 4:
        count_h = 0
        count_v = 0
        for i in range(0, len(x), 3):
            list1.append(x[i:i + 3])
        #print(who_is_next, x,list1)
    # spaces or empty
    # Draw
    # wins
        h_win = 0
        v_win = 0
        for i in range(0, 3):
            # horizontal win
            h_x = list1[i].count('X')
            h_o = list1[i].count('O')
            h_win += who_wins(h_x, h_o)
            vertical = [v[i] for v in list1]
            v_o = vertical.count('O')
            v_x = vertical.count('X')
            v_win += who_wins(v_x, v_o)

        if h_win == 3 and v_win == 3:
            d_x = 0
            d_o = 0
            # diagonal win
            for i in range(0, 3):
                d_x += list1[i][i].count('X')
                d_o += list1[i][i].count('O')
            if who_wins(d_x, d_o) == 1:
                d_x = [list1[0][2], list1[1][1], list1[2][0]].count('X')
                d_o = [list1[0][2], list1[1][1], list1[2][0]].count('O')
            if who_wins(d_x, d_o) == 1:  # draw
                if x.count('X') + x.count('O') == 9:
                    if x.count('X') == 5 and x.count('O') == 4:
                        print_tic_tac_toe(x)
                        print('Draw')
                        sys.exit()
                    elif x.count('O') == 5 and x.count('X') == 4:
                        print_tic_tac_toe(x)
                        print('Draw')
                        sys.exit()

'''

count_h = 0
count_v = 0
for i in range(0, len(x), 3):
    list1.append(x[i:i + 3])
# Impossible
if abs(x.count('X') - x.count('O')) > 1:
    print_tic_tac_toe(x)
    print('Impossible')
    sys.exit()
else:
    for i in range(0, 3):
        h_x = list1[i].count('X')
        h_o = list1[i].count('O')
        if h_x == 3:

            count_h += 1
        elif h_o == 3:
            count_h += 1
        vertical = [v[i] for v in list1]
        v_o = vertical.count('O')
        v_x = vertical.count('X')
        if v_x == 3:
            count_v += 1
        elif v_o == 3:
            count_v += 1
    if count_h > 1 or count_v > 1:
        print_tic_tac_toe(x)
        print('Impossible')
        sys.exit()

# spaces or empty
# Draw
# wins
h_win = 0
v_win = 0
for i in range(0, 3):
    # horizontal win
    h_x = list1[i].count('X')
    h_o = list1[i].count('O')
    h_win += who_wins(h_x, h_o, x)
    vertical = [v[i] for v in list1]
    v_o = vertical.count('O')
    v_x = vertical.count('X')
    v_win += who_wins(v_x, v_o, x)

if h_win == 3 and v_win == 3:
    d_x = 0
    d_o = 0
    # diagonal win
    for i in range(0, 3):
        d_x += list1[i][i].count('X')
        d_o += list1[i][i].count('O')
    if who_wins(d_x, d_o, x) == 1:
        d_x = [list1[0][2], list1[1][1], list1[2][0]].count('X')
        d_o = [list1[0][2], list1[1][1], list1[2][0]].count('O')
    if who_wins(d_x, d_o, x) == 1:  # draw
        if x.count('X') + x.count('O') == 9:
            if x.count('X') == 5 and x.count('O') == 4:
                print_tic_tac_toe(x)
                print('Draw')
                sys.exit()
            elif x.count('O') == 5 and x.count('X') == 4:
                print_tic_tac_toe(x)
                print('Draw')
                sys.exit()
        elif x.count('_') != 0:
            print_tic_tac_toe(x)
            print('Game not finished')
            sys.exit()
'''