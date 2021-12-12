with open('./05', 'r') as f: lines = f.read().splitlines()
straight_coords, diag_coords = [], []
max_x, max_y = 0, 0
for line in lines:
    x1, y1 = int(line.split(' -> ')[0].split(',')[0]), int(line.split(' -> ')[0].split(',')[1])
    x2, y2 = int(line.split(' -> ')[1].split(',')[0]), int(line.split(' -> ')[1].split(',')[1])
    for x in [x1, x2]:
        if x > max_x: max_x = x
    for y in [y1, y2]:
        if y > max_y: max_y = y
    if x1 != x2 and y1 != y2: diag_coords.append(((x1,y1),(x2,y2)))
    else: straight_coords.append(((x1,y1),(x2,y2)))
#print(straight_coords)

grid = []
for i in range(0, max_y+1): grid.append([0] * (max_x+1))

#print(grid)
for pair in straight_coords:
    x1, x2, y1, y2 = pair[0][0], pair[1][0], pair[0][1], pair[1][1]

    if y1 == y2:
        # Horizontal line
        #print("y value stays the same")
        for i in range(min(x1,x2), max(x1,x2)+1, 1):
            #print(f"{x1=},{y1=}  {x2=},{y2=}  {i=}")
            grid[y1][i] += 1
    elif x1 == x2:
        # Vertical line
        #print("x value stays the same")
        for i in range(min(y1,y2), max(y1,y2)+1, 1):
            #print(f"{x1=},{y1=}  {x2=},{y2=}  {i=}")
            grid[i][x1] += 1
    else:
        print("something is very wrong")

for pair in diag_coords:
    x1, x2, y1, y2 = pair[0][0], pair[1][0], pair[0][1], pair[1][1]
    # options for diag: 00, 01, 10, 11 (x down y down, x down y up, x up y down, x up y up)
    if x1 < x2 and y1 < y2: # 11
        if x2 - x1 != y2 - y1:
            print(f'{x2 - x1} {y2 - y1}')
        for i in range(0, x2-x1+1):
            grid[y1+i][x1+i] += 1

    elif x1 < x2 and y1 > y2: # 10
        if x2 - x1 != y1 - y2:
            print(f'{x1 - x2} {y1 - y2}')
        for i in range(0, x2-x1+1):
            grid[y1-i][x1+i] += 1

    elif x1 > x2 and y1 < y2: # 01
        if x1 - x2 != y2 - y1:
            print(f'{x1 - x2} {y1 - y2}')
        for i in range(0, x1-x2+1):
            grid[y1+i][x1-i] += 1

    elif x1 > x2 and y1 > y2: # 00
        if x1 - x2 != y1 - y2:
            print(f'{x1 - x2} {y1 - y2}')
        for i in range(0, x1-x2+1):
            grid[y1-i][x1-i] += 1
    else:
        print("something is very wrong again")

overlaps = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] > 1: overlaps += 1
        if grid[i][j] == 0: grid[i][j] = '.'
    print(''.join(str(x) for x in grid[i]))
    
print(overlaps)