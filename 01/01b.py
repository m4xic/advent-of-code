with open('input', 'r') as f:
    raw = f.readlines()
    instructions = [x.strip() for x in raw]

print(instructions)

dial = 50
counter = 0

for instruction in instructions:
    print()
    multiple_rotations = False
    direction, amount = instruction[0], int(instruction[1:])
    rotations = 0
    print(f'{dial=}{'-' if direction == "L" else '+'}{amount}\nbefore {counter=}')
    if direction == "L":
        if dial == 0: rotations = -1
        dial -= amount
    else:
        dial += amount

    while dial > 100:
        dial -= 100
        rotations += 1

    while dial < 0:
        dial += 100
        rotations += 1

    if dial == 100: dial = 0

    if dial == 0: rotations += 1

    print(f'new {dial=} {rotations=}')
    
    counter += rotations

    print(f'after {counter=}')
print(counter)
