with open(r'AC\AC2.txt', 'r') as f:
    list_pass = f.read().split('\n')

ct = 0
for e in list_pass:
    spl = e.split(':')
    spll = spl[0].split(' ')
    target = spll[1]
    min_occ, max_occ = spll[0].split('-')
    passw = spl[1].replace(' ', '')
    c = 0
    if passw[int(min_occ)-1] == target and passw[int(max_occ)-1] != target:
        ct += 1
    if passw[int(min_occ)-1] != target and passw[int(max_occ)-1] == target:
        ct += 1

print(ct)