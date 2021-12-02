with open('01', 'r') as f:
    numbers = f.read().splitlines()
    increased = 0
    for i in range(3, len(numbers)):
        first_set = int(numbers[i-3]) + int(numbers[i-2]) + int(numbers[i-1])
        second_set = int(numbers[i-2]) + int(numbers[i-1]) + int(numbers[i])
        if first_set < second_set: increased += 1
print(increased)