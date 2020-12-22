
def find_matches(list_nr, match):
    for elt in list_nr:
        if match-elt in list_nr:
            return True
    return False


with open(r'AC\AC9.txt', 'r') as f:
    list_nrs = [int(nr) for nr in f.read().split('\n')]

window = 25
wanted = 0

for i in range(window, len(list_nrs)):
    if not find_matches(list_nrs[i-window:i], list_nrs[i]):
        wanted = list_nrs[i]
        break

for i in range(len(list_nrs)):
    current_sum = 0
    j = i
    while current_sum < wanted:
        current_sum += list_nrs[j]
        j += 1
    if current_sum == wanted:
        print(min(list_nrs[i:j])+max(list_nrs[i:j]))
        break
