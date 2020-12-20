import re


def is_nr(val, min_val, max_val):
    if not val.isdigit():
        return False
    if min_val <= int(val) <= max_val:
        return True
    else:
        return False


def is_year(val, min_val, max_val):
    if len(val) != 4 or not is_nr(val, min_val, max_val):
        return False
    else:
        return True


def is_height(val):
    if val[-2:] == 'cm':
        return is_nr(val[:-2], 150, 193)
    if val[-2:] == 'in':
        return is_nr(val[:-2], 59, 76)
    return False


def is_hc(val):
    if re.match('^#[0-9a-f]{6}$', val):
        return True
    return False


def is_ec(val):
    if len(val) != 3:
        return False
    if re.match('amb|blu|brn|gry|grn|hzl|oth', val):
        return True
    return False


def is_pid(val):
    if len(val) != 9 or not val.isdigit():
        return False
    return True


with open(r'C:\Users\t-caneg\Desktop\AC\AC4.txt', 'r') as f:
    list_p = f.read().split('\n\n')


ct = 0
need = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for p in list_p:
    fields = p.split()
    dict_pass = dict()
    for field in fields:
        key, val = field.split(':')
        dict_pass[key] = val
    if not set(need).issubset(dict_pass.keys()):
        continue
    if not is_year(dict_pass['byr'], 1920, 2020):
        continue
    if not is_year(dict_pass['iyr'], 2010, 2020):
        continue
    if not is_year(dict_pass['eyr'], 2020, 2030):
        continue
    if not is_height(dict_pass['hgt']):
        continue
    if not is_hc(dict_pass['hcl']):
        continue
    if not is_ec(dict_pass['ecl']):
        continue
    if not is_pid(dict_pass['pid']):
        continue
    ct += 1

print(ct)





