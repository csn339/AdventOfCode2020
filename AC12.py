import numpy
import re


def rules(facing, NS_val, EW_val, rule, val):
    dir = ['E', 'S', 'W', 'N']
    if rule == 'N':
        NS_val += val
    if rule == 'S':
        NS_val -= val
    if rule == 'E':
        EW_val += val
    if rule == 'W':
        EW_val -= val
    if rule == 'L':
        nr_steps = (dir.index(facing) - val/90) % 4
        facing = dir[int(nr_steps)]
    if rule == 'R':
        nr_steps = (dir.index(facing) + val/90) % 4
        facing = dir[int(nr_steps)]
    if rule == 'F':
        facing, NS_val, EW_val = rules(facing, NS_val, EW_val, facing, val)
    return facing, NS_val, EW_val


def rules2(NS_ship, EW_ship, NS_wp, EW_wp, rule, val):

    if rule == 'N':
        NS_wp += val
    if rule == 'S':
        NS_wp -= val
    if rule == 'E':
        EW_wp += val
    if rule == 'W':
        EW_wp -= val
    if rule == 'L':
        EW_wp_new = EW_wp*numpy.cos(numpy.pi*val/180) - NS_wp*numpy.sin(numpy.pi*val/180)
        NS_wp_new = EW_wp*numpy.sin(numpy.pi*val/180) + NS_wp*numpy.cos(numpy.pi*val/180)
        EW_wp = EW_wp_new
        NS_wp = NS_wp_new
    if rule == 'R':
        EW_wp_new = EW_wp*numpy.cos(numpy.pi*val/180) + NS_wp*numpy.sin(numpy.pi*val/180)
        NS_wp_new = -EW_wp*numpy.sin(numpy.pi*val/180) + NS_wp*numpy.cos(numpy.pi*val/180)
        EW_wp = EW_wp_new
        NS_wp = NS_wp_new
    if rule == 'F':
        NS_ship += NS_wp * val
        EW_ship += EW_wp * val

    return NS_ship, EW_ship, NS_wp, EW_wp


with open(r'AC\AC12.txt', 'r') as f:
    list_com = f.read().split('\n')

NS_ship, EW_ship, NS_wp, EW_wp = 0, 0, 1, 10

for elt in list_com:
    rule = re.findall('N|S|E|W|L|R|F', elt)[0]
    val = int(elt.replace(rule, ''))
    NS_ship, EW_ship, NS_wp, EW_wp = rules2(NS_ship, EW_ship, NS_wp, EW_wp, rule, val)
    print(NS_ship, EW_ship, NS_wp, EW_wp)

print(round(abs(NS_ship)+abs(EW_ship)))




