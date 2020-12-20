with open(r'C:\Users\t-caneg\Desktop\AC\AC1.txt', 'r') as f:
    list_nrs = f.read().split('\n')

list_nrs = [int(elt) for elt in list_nrs]
nrs_sort = sorted(list_nrs)

for k in range(len(nrs_sort)):
    chosen = nrs_sort[k]
    new_list = nrs_sort[k:]
    to_find = 2020-chosen
    amount_rejected = 0
    for i in range(len(new_list)):
        rejected_count = 0
        for j in range(amount_rejected + 1, len(new_list)):
            if new_list[i] + new_list[-j] > to_find:
                rejected_count += 1
                continue
            elif new_list[i] + new_list[-j] == to_find:
                print(new_list[i] * new_list[-j]*chosen)
                break
            else:
                amount_rejected += rejected_count
                break



