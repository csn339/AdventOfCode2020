
def count_trees(list_lines, rows, cols):
    ct_tree = 0
    pos = 0
    max_len = len(list_lines[0])

    for i in range(0, len(list_lines), rows):
        line = list_lines[i]
        if pos > max_len-1:
            var = pos % max_len
        else:
            var = pos
        if line[var] == '#':
            ct_tree += 1
        pos += cols

    return ct_tree


if __name__ == "__main__":

    with open(r'AC\AC3.txt', 'r') as f:
        list_lines = f.read().split('\n')

    print(count_trees(list_lines, 1, 3)*count_trees(list_lines, 1, 1)*count_trees(list_lines, 1, 5)*count_trees(list_lines, 1, 7)*count_trees(list_lines, 2, 1))

