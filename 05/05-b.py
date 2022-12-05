with open('input-main', 'r') as fp:
    file = fp.readlines()

pivot = file.index('\n')
grid, instructions = [i.rstrip() for i in file[:pivot]], [i.rstrip() for i in file[pivot+1:]]

columns = [1,5,9,13,17,21,25,29,33]
piles = [[], [], [], [], [], [], [], [], []]

height = len(grid) - 1
for y in range(2, height + 2):
    for x in range(9):
        if grid[-y][columns[x]] != ' ':
            piles[x].append(grid[-y][columns[x]])
print(piles)

for inst in instructions:
    _, num, _, from_pile, _, to_pile = [int(i) if i.isnumeric() else "" for i in inst.split(' ')]

    popped, piles[from_pile-1] = piles[from_pile-1][-num:][::-1], piles[from_pile-1][:-num]
    print(inst, 'popped', popped, f"({num})", 'from', from_pile)
    while popped:
        crate = popped.pop()
        piles[to_pile-1].append(crate)

print(piles)
for k in piles:
    print(k[-1])
