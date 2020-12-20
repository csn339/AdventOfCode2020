with open(r'AC\AC5.txt', 'r') as f:
    list_nrs = f.read().split('\n')

max_nr = 0
list_seats = []

for p in list_nrs:
    row_r = 127
    row_l = 0
    col_r = 7
    col_l = 0
    for char in p:
        if char == 'F':
            row_r = row_r-(row_r-row_l+1)//2
        if char == 'B':
            row_l = row_r-(row_r-row_l+1)//2+1
        if char == 'R':
            col_l = col_r-(col_r-col_l+1)//2+1
        if char == 'L':
            col_r = col_r-(col_r-col_l+1)//2
    if col_l != col_r or row_l != row_r:
        print('failed')
    if row_r*8 + col_r > max_nr:
        max_nr = row_r*8 + col_r
    list_seats.append(row_r*8 + col_r)

list_new = sorted(list_seats)
for i in range(len(list_new)-1):
    if list_new[i+1]-list_new[i] == 2:
        print(list_new[i])