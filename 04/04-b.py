with open('input', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

overlap = 0
for line in lines:
    a_line, b_line = line.split(',')

    # otherwise compares them as strings :/
    a_low, a_high = [int(i) for i in a_line.split('-')]
    b_low, b_high = [int(i) for i in b_line.split('-')]

    a = range(a_low, a_high+1)
    b = range(b_low, b_high+1)
    intersection = list(set(a) & set(b))
    if intersection:
        overlap += 1

print(overlap)
