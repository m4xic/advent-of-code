with open('input', 'r') as fp:
    file = fp.readlines()
    pairs = []
    for line in file:
        line = line.strip()
        pairs.append(line.split(' '))

# A = rock (1)
# B = paper (2)
# C = scissors (3)

# Z win = 6, Y draw = 3, X lose = 0

win_vs = {'A': 'B', 'B': 'C', 'C': 'A'}
drw_vs = {'A': 'A', 'B': 'B', 'C': 'C'}
lse_vs = {'A': 'C', 'B': 'A', 'C': 'B'}
points = {'A': 1, 'B': 2, 'C': 3}

total = 0
for pair in pairs:
    if pair[1] == 'Z':
        total += 6
        total += points[win_vs[pair[0]]]
    elif pair[1] == 'Y':
        total += 3
        total += points[drw_vs[pair[0]]]
    elif pair[1] == 'X':
        total += 0
        total += points[lse_vs[pair[0]]]
print(total)
