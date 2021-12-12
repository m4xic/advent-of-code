with open('./05', 'r') as f: lines = f.read().splitlines()
coords = []
max_x, max_y = 0, 0
for line in lines:
    x1, y1 = int(line.split(' -> ')[0].split(',')[0]), int(line.split(' -> ')[0].split(',')[1])
    x2, y2 = int(line.split(' -> ')[1].split(',')[0]), int(line.split(' -> ')[1].split(',')[1])
    for x in [x1, x2]:
        if x > max_x: max_x = x
    for y in [y1, y2]:
        if y > max_y: max_y = y
    if x1 != x2 and y1 != y2: print(f"Ignoring diagonal {x1=},{y1=} {x2=},{y2=}")
    else: coords.append(((x1,y1),(x2,y2)))
#print(coords)

grid = []
for i in range(0, max_y+1): grid.append([0] * (max_x+1))

#print(grid)
for pair in coords:
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

overlaps = 0
for line in grid:
    for square in line:
        if square > 1: overlaps += 1
print(overlaps)