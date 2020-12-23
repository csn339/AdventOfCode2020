def adjust_seating(row, col, list_r):
    neighbours = [list_r[row][col+1], list_r[row][col-1], list_r[row+1][col+1], list_r[row+1][col], list_r[row+1][col-1],
                  list_r[row-1][col+1], list_r[row-1][col], list_r[row-1][col-1]]
    ct_full = 0
    if list_r[row][col] == 'L':
        flag = [(n == 'L' or n == '-' or n=='.') for n in neighbours]
        if False not in flag:
            return '#'
    elif list_r[row][col] == '#':
        for n in neighbours:
            if n == '#':
                ct_full += 1
            if ct_full > 3:
                return 'L'
    return list_r[row][col]


def is_neighbour(list_r, row, col, inc, pos):
    if pos == 0:
        return list_r[row][col+inc]
    if pos == 1:
        return list_r[row][col - inc]
    if pos == 2:
        return list_r[row+inc][col+inc]
    if pos == 3:
        return list_r[row+inc][col]
    if pos == 4:
        return list_r[row+inc][col-inc]
    if pos == 5:
        return list_r[row-inc][col+inc]
    if pos == 6:
        return list_r[row-inc][col]
    if pos == 7:
        return list_r[row-inc][col-inc]


def adjust_seating_seen(row, col, list_r):
    inc = 1
    vals = []
    nr_neighbours = 8
    for i in range(nr_neighbours):
        while is_neighbour(list_r, row, col, inc, i) == '.':
            inc += 1
        vals.append(is_neighbour(list_r, row, col, inc, i))
        inc = 1

    ct_full = 0
    if list_r[row][col] == 'L':
        flag = [(n == 'L' or n == '-' or n == '.') for n in vals]
        if False not in flag:
            return '#'
    elif list_r[row][col] == '#':
        for n in vals:
            if n == '#':
                ct_full += 1
            if ct_full > 4:
                return 'L'
    return list_r[row][col]


def pad(list_rows):
    list_ext = []
    list_ext.append('-' * (len(list_rows[1]) + 2))
    for i in range(len(list_rows)):
        list_ext.append('-' + list_rows[i] + '-')
    list_ext.append('-' * (len(list_rows[1]) + 2))
    return list_ext


with open(r'AC\AC11.txt', 'r') as f:
    list_rows = f.read().split('\n')


list_past = pad(list_rows).copy()
list_new = [''] * len(list_rows)

flag = True
while flag:
    flag = False
    list_new = [''] * len(list_rows)
    for row in range(1, len(list_rows)+1):
        for col in range(1, len(list_rows[1])+1):
            char = adjust_seating_seen(row, col, list_past)
            list_new[row-1] += char
            if list_past[row][col] != char:
                flag = True
    list_past = pad(list_new).copy()

ct_occupied = 0
for row in range(len(list_rows)):
    for col in range(len(list_rows[1])):
        if list_new[row][col] == '#':
            ct_occupied += 1
print(ct_occupied)
