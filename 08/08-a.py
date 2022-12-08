with open('input', 'r') as fp:
    grid = [i.strip() for i in fp.readlines()]

visible = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):

        left, right, top, bottom = True, True, True, True

        # check left, y remains same
        for xr in range(0, x):
            if xr == x and y == y:
                continue
            if grid[y][xr] >= grid[y][x]:
                left = False

        # check top, x remains same
        for yr in range(0, y):
            if yr == y and x == x:
                continue
            if grid[yr][x] >= grid[y][x]:
                top = False

        # check right, y remains same
        for xr in range(x, len(grid[y])):
            if xr == x and y == y:
                continue
            if grid[y][xr] >= grid[y][x]:
                right = False

        # check bottom, x remains same
        for yr in range(y, len(grid)):
            if yr == y and x == x:
                continue
            if grid[yr][x] >= grid[y][x]:
                bottom = False

        vis = left or right or top or bottom
        if vis:
            visible += 1

        print(
            f"({y+1},{x+1}) = {grid[y][x]} | {vis=} | {left=} {right=} {top=} {bottom=}")

print(visible)
