with open('02', 'r') as f:
    directions = f.read().splitlines()

x, y = 0, 0

for line in directions:
    way, amount = line.split()[0], int(line.split()[1])
    if way == "forward":
        x += amount
    elif way == "backward":
        x -= amount
    elif way == "up":
        y -= amount
    elif way == "down":
        y += amount
    else:
        print(f"Didn't recognise that direction {way} {amount}")

print(f"{x=} {y=}")