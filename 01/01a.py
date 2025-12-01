with open('input', 'r') as f:
    raw = f.readlines()
    instructions = [x.strip() for x in raw]

print(instructions)

dial = 50
counter = 0

for instruction in instructions:
    direction, amount = instruction[0], int(instruction[1:])
    if direction == "L":
        dial -= amount
    else:
        dial += amount

    while dial > 99:
        dial -= 100

    while dial < 0:
        dial += 100

    print(f'{dial=}')
    
    if dial == 0:
        counter += 1

print(counter)
