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

        factors = []
        for i in range(1, len(num_as_string)):
            if len(num_as_string) % i == 0: factors.append(i)

        for factor in factors:
            
            part = num_as_string[:factor]
            #print(f'{num_as_string=} {factor=} {part=}')

            test_string = part * int(len(num_as_string) / factor)
            if test_string == num_as_string:
                invalid.append(number)
                #print(f"** FOUND ONE! {test_string=} {num_as_string=} {factor=} {part=}")


print(invalid)
print(sum(set(invalid)))