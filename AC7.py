import re


def score(dict_, key):
    scored = 0
    for key2 in dict_[key]:
        if key2 == 'other':
            scored += 0
        else:
            scored += int(dict_[key][key2])+int(dict_[key][key2])*score(dict_, key2)
    return scored


with open(r'AC\AC7.txt', 'r') as f:
    list_rules = f.read().split('\n')

dict_rules = dict(dict())

for rule in list_rules:
    key, vals = rule.split('contain')
    key = key.replace(' bags', '')
    key = key.strip()
    dict_rules[key] = dict()
    val_list = vals.split(',')
    for elt in val_list:
        elt = elt.strip()
        nr = elt[0]
        key_val = re.sub('bags|bag|\\.', '', elt[2:])
        key_val = key_val.strip()
        dict_rules[key][key_val] = nr

col = 'shiny gold'
matched = set([col])
flag = True
current_ct = 0
to_visit = set(dict_rules.keys())
while flag:
    for key in to_visit:
        if len(matched.intersection(set(dict_rules[key]))) == 0:
            continue
        matched.add(key)
    if current_ct != len(matched):
        current_ct = len(matched)
        to_visit = to_visit-matched
    else:
        flag = False

print(current_ct-1)
print(score(dict_rules, col))




