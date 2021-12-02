with open('02', 'r') as f:
    directions = f.read().splitlines()

x, y, aim = 0, 0, 0

for line in directions:
    way, amount = line.split()[0], int(line.split()[1])
    if way == "forward":
        x += amount
        y += aim * amount
        print(f"FORWARD: {x=} {y=} {amount=} {aim=}")
    elif way == "up":
        aim -= amount
        print(f"UP: {x=} {y=} {amount=} {aim=}")
    elif way == "down":
        aim += amount
        print(f"DOWN: {x=} {y=} {amount=} {aim=}")
    else:
        print(f"Didn't recognise that direction {way} {amount}")

print(f"{x=} {y=} {aim=} {x*y=}")