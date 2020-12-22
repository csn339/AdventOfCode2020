from collections import defaultdict

with open(r'AC\AC10.txt', 'r') as f:
    list_nrs = [int(nr) for nr in f.read().split('\n')]

list_sorted = sorted(list_nrs)
ct_1 = ct_3 = 0

if list_sorted[0] == 1:
    ct_1 += 1
elif list_sorted[0] == 3:
    ct_3 += 1

for i in range(len(list_sorted)-1):
    if list_sorted[i+1] - list_sorted[i] == 1:
        ct_1 += 1
    elif list_sorted[i+1] - list_sorted[i] == 3:
        ct_3 += 1
    elif list_sorted[i+1] - list_sorted[i] > 3:
        print("issue")
        break
# print(ct_1*(ct_3+1))

count_map =defaultdict(int)
count_map[0] = 1

for i in range(len(list_sorted)):
    target = list_sorted[i]
    count_map[target] = count_map[target-1]+count_map[target-2]+count_map[target-3]

print(count_map[list_sorted[-1]])

