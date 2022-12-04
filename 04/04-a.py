with open('input', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

contained = 0
for line in lines:
    a, b = line.split(',')

    # otherwise compares them as strings :/
    a_low, a_high = [int(i) for i in a.split('-')]
    b_low, b_high = [int(i) for i in b.split('-')]

    if b_low <= a_low and a_high <= b_high:
        print(line, 'a inside b', a_low, a_high, b_low, b_high)
        contained += 1
    elif a_low <= b_low and b_high <= a_high:
        print(line, 'b inside a', a_low, a_high, b_low, b_high)
        contained += 1
    else:
        print(line, 'not fully contained')

print(contained)
