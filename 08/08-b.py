with open('input', 'r') as fp:
    grid = [i.strip() for i in fp.readlines()]

scenics = []

visible = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):

        left, right, top, bottom = True, True, True, True
        l_sc, r_sc, t_sc, b_sc = 0, 0, 0, 0

        # check left, y remains same
        for xr in range(0, x)[::-1]:
            if xr == x and y == y:
                continue
            if grid[y][xr] >= grid[y][x]:
                left = False
                l_sc += 1
                break
            else:
                l_sc += 1

        # check top, x remains same
        for yr in range(0, y)[::-1]:
            if yr == y and x == x:
                continue
            if grid[yr][x] >= grid[y][x]:
                top = False
                t_sc += 1
                break
            else:
                t_sc += 1

        # check right, y remains same
        for xr in range(x, len(grid[y])):
            if xr == x and y == y:
                continue
            if grid[y][xr] >= grid[y][x]:
                right = False
                r_sc += 1
                break
            else:
                r_sc += 1

        # check bottom, x remains same
        for yr in range(y, len(grid)):
            if yr == y and x == x:
                continue
            if grid[yr][x] >= grid[y][x]:
                bottom = False
                b_sc += 1
                break
            else:
                b_sc += 1

        vis = left or right or top or bottom
        if vis:
            visible += 1
        scenic = l_sc * r_sc * t_sc * b_sc
        scenics.append(scenic)

        print(
            f"({y+1},{x+1}) = {grid[y][x]} | {vis=} | {scenic=} | {l_sc=} {r_sc=} {t_sc=} {b_sc=}")

print(visible)
print(max(scenics))
