with open(r'AC\AC8.txt', 'r') as f:
    list_rules = f.read().split('\n')

commands = []
nrs = []

for elt in list_rules:
    commands.append(elt.split(' ')[0])
    nrs.append(elt.split(' ')[1])
print(commands)

flag = False
change = -1
config = commands.copy()

while not flag:
    current_val = 0
    visited = [False]*len(commands)
    i = 0
    while not visited[i]:
        visited[i] = True
        if config[i] == 'nop':
            i += 1
        elif config[i] == 'acc':
            current_val += int(nrs[i])
            i += 1
        else:
            i += int(nrs[i])
        if i >= len(commands):
            print(current_val)
            flag = True
            break

    if not flag:
        config[:change + 1] = commands[:change + 1]
        for j in range(change + 1, len(commands)):
            if commands[j] == 'nop':
                config[j] = 'jmp'
                change = j
                break
            elif commands[j] == 'jmp':
                config[j] = 'nop'
                change = j
                break
