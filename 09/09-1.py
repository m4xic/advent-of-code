with open('09', 'r') as f: grid = f.read().splitlines()
for i in range(0, len(grid)): grid[i] = [9] + [int(height) for height in list(grid[i])] + [9]
grid.insert(0, [9] * len(grid[0]))
grid.append([9] * len(grid[0]))

weak_points, risk = 0, 0
for y in range(1, len(grid)-1):
    for x in range(1, len(grid[0])-1):
        me = grid[y][x]
        if grid[y-1][x] > me and grid[y][x-1] > me and grid[y+1][x] > me and grid[y][x+1] > me:
            weak_points += 1
            risk += 1 + me
print(f"{weak_points=}  {risk=}")