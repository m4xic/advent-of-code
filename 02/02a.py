with open('input', 'r') as f:
    full_list = f.read().strip()

print(full_list)

ranges = full_list.split(',')
print(ranges)

invalid = []

for range_set in ranges:
    start, end = [int(x) for x in range_set.split('-')]
    #print(f'{start=}, {end=}')

    for number in range(start, end+1):
        #print(number)
        num_as_string = str(number)
        midpoint = len(num_as_string) // 2
        first_half = num_as_string[:midpoint]
        last_half = num_as_string[midpoint:]

        #print(first_half, last_half)
        if first_half == last_half:
            invalid.append(number)

print(invalid)
print(sum(invalid))