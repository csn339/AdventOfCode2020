from collections import defaultdict

with open(r'AC\AC15.txt', 'r') as f:
    start_nrs = f.read().split(',')

turns = len(start_nrs)
last_seen = start_nrs[-1]
seen_dict = defaultdict(tuple)
for i in range(len(start_nrs)):
    seen_dict[start_nrs[i]] = (i+1, i+1)

while turns < 30000000:
    if last_seen not in seen_dict:
        last_seen = '0'
    else:
        last_seen = str(seen_dict[last_seen][1] - seen_dict[last_seen][0])
    turns += 1
    if last_seen in seen_dict:
        last_max = seen_dict[last_seen][1]
        seen_dict[last_seen] = (last_max, turns)
    else:
        seen_dict[last_seen] = (turns, turns)

print(last_seen)

