from collections import defaultdict


def join_intervals(a:list):
    b = []
    for begin, end in sorted(a):
        if b and b[-1][1] >= begin - 1:
            b[-1][1] = max(b[-1][1], end)
        else:
            b.append([begin, end])
    return b


def check_in_range(a:list, nr:int):
    for range in a:
        if range[0] <= nr <= range[1]:
            return True
    return False


def check_in_instruction(a: list, dict_ins: dict):
    keep = list(dict_ins.keys())
    ban = []
    for elt in a:
        for e in keep:
            range1, range2 = dict_ins[e][0], dict_ins[e][1]
            if not (range1[0] <= int(elt) <= range1[1] or range2[0] <= int(elt) <= range2[1]):
                ban.append(e)
        keep = [key for key in keep if key not in ban]
    return keep


def resolve_unique_mapping(a: list):
    resolved = ['0']*len(a)
    ct = 0
    while ct < 20:
        for i in range(len(a)):
            if len(a[i]) == 1 and resolved[i] == '0':
                resolved[i] = a[i][0]
                ct += 1
                for j in range(len(a)):
                    if resolved[i] in a[j]:
                        new_elt = [elt for elt in a[j] if elt != resolved[i]]
                        a[j] = new_elt
    return resolved


with open(r'AC\AC16.txt', 'r') as f:
    list_commands = f.read().split('\n')

list_instructions = list_commands[:20]
my_ticket = list_commands[22]
nearby_tickets = list_commands[25:]

dict_instructions = defaultdict(list)

for elt in list_instructions:
    name, ranges = elt.split(': ')
    range1, range2 = ranges.split(' or ')
    range1 = tuple([int(elt) for elt in range1.split('-')])
    range2 = tuple([int(elt) for elt in range2.split('-')])
    dict_instructions[name] = [range1, range2]

list_intervals = []
for key in dict_instructions:
    list_intervals.extend(dict_instructions[key])
list_to_check = join_intervals(list_intervals)

list_banned = []
for ticket in nearby_tickets:
    list_nrs = [int(elt) for elt in ticket.split(',')]
    for nr in list_nrs:
        if not check_in_range(list_to_check, nr):
            list_banned.append(ticket)

kept_tickets = [t for t in nearby_tickets if t not in list_banned]

step_1 = []
for i in range(20):
    pos_nrs = []
    for ticket in kept_tickets:
        list_nrs = [int(elt) for elt in ticket.split(',')]
        pos_nrs.append(list_nrs[i])
    step_1.append(check_in_instruction(pos_nrs, dict_instructions))

prod = 1
my_list_nrs = [int(elt) for elt in my_ticket.split(',')]
step_2 = resolve_unique_mapping(step_1)
for i in range(len(step_2)):
    if 'departure' in step_2[i]:
        prod *= my_list_nrs[i]

print(prod)

