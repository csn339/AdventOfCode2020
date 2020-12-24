# Chinese Remainder Theorem from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6

from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def find_min(buses, target):
    to_wait = [bus - target % bus for bus in buses]
    return buses[to_wait.index(min(to_wait))]*min(to_wait)


with open(r'AC\AC13.txt', 'r') as f:
    list_start = f.read().split('\n')
target = int(list_start[0])
list_temp = list_start[1].split(',')
bus_options = [int(elt) for elt in list_temp if elt != 'x']
print(find_min(bus_options, target))

rem = []
div = []
for i in range(len(list_temp)):
    if list_temp[i].isdigit():
        rem.append(int(list_temp[i])-i)
        div.append(int(list_temp[i]))

print(chinese_remainder(div, rem))


