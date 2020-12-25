import re


def decimalToBinary(n: int):
    rep = bin(n).replace("0b", "")
    return '0'*(36-len(rep)) + rep


def binaryToDecimal(n: str):
    return int(n, 2)


def do_addition(val, mask):
    result = ''
    for i in range(len(mask)):
        if mask[i] == 'X':
            result += val[i]
        else:
            result += mask[i]
    return result


def trans_x(list_r):
    list_t = []
    for elt in list_r:
        temp = elt.split('X',1)
        list_t.append(temp[0]+'0'+temp[1])
        list_t.append(temp[0]+'1'+temp[1])
    return list_t


def change_address(addr, mask):
    result = ''
    for i in range(len(mask)):
        if mask[i] == 'X':
            result += 'X'
        elif mask[i] == '0':
            result += addr[i]
        else:
            result += '1'
    list_res = [result]
    while 'X' in list_res[0]:
        list_res = trans_x(list_res)
    return [binaryToDecimal(elt) for elt in list_res]


with open(r'AC\AC14.txt', 'r') as f:
    list_commands = f.read().split('\n')

mem = dict()
mem2 = dict()
mask = 0
for line in list_commands:
    if 'mask' in line:
        mask = line.replace('mask = ', '')
    else:
        match = re.search(r'.*?\[(.*)].*', line)
        loc = match.group(1)
        val = line.split(' = ')[1]
        val_bin = decimalToBinary(int(val))
        mem[loc] = do_addition(val_bin, mask)
        val_loc = decimalToBinary(int(loc))
        list_loc = change_address(val_loc, mask)
        for elt in list_loc:
            mem2[elt] = val

sum_vals = 0
for key in mem:
    sum_vals += binaryToDecimal(str(mem[key]))

sum_vals2 = 0

for key in mem2:
    sum_vals2 += int(mem2[key])

print(sum_vals)
print(sum_vals2)



