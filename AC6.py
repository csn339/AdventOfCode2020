with open(r'AC\AC6.txt', 'r') as f:
    list_ans = f.read().split('\n\n')

total_yes = 0
total_all_yes = 0
for ans in list_ans:
    ans_ = ans.replace('\n', '')
    unique_ans = len(set(ans_))
    total_yes += unique_ans
    ans2 = ans.split('\n')
    in_common = set(ans2[0])
    for a in ans2[1:]:
        in_common = in_common.intersection(set(a))
    total_all_yes += len(in_common)
print(total_all_yes)
print(total_yes)