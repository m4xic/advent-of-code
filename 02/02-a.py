with open('input', 'r') as fp:
    file = fp.readlines()
    pairs = []
    for line in file:
        line = line.strip()
        pairs.append(line.split(' '))

# A/X = rock (1)
# B/Y = paper (2)
# C/Z = scissors (3)

# win = 6, draw = 3, lose = 0

player_wins = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
player_draw = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
player_loss = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]
player_points = {'X': 1, 'Y': 2, 'Z': 3}

points = 0
for pair in pairs:
    if pair in player_wins:
        points += 6
    elif pair in player_draw:
        points += 3
    points += player_points[pair[1]]
print(points)
