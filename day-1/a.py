with open('input-a', 'r') as file:
    numbers = file.readlines()
    for x in range(0, len(numbers)): numbers[x] = int(numbers[x].strip())

    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
                if numbers[i] == numbers[j]: continue
                elif numbers[i] + numbers[j] == 2020:
                    print(numbers[i] * numbers[j])
                else: continue