with open('input-a', 'r') as file:
    numbers = file.readlines()
    for x in range(0, len(numbers)): numbers[x] = int(numbers[x].strip())

    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            for k in range(0, len(numbers)):
                if numbers[i] == numbers[j] or numbers[i] == numbers[k] or numbers[k] == numbers[j]: continue
                elif numbers[i] + numbers[j] + numbers[k] == 2020:
                    print(numbers[i] * numbers[j] * numbers[k])
                else: continue