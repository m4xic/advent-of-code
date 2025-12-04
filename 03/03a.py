with open('input', 'r') as f:
    batteries = [list(x.strip()) for x in f.readlines()]

total_joltage = 0

for battery in batteries:
    largest_so_far = 0

    for i in range(len(battery)):
        usable_list = battery[i+1:]
        if usable_list:
            for j in range(len(usable_list)):
                tested_number = int(f"{battery[i]}{battery[i+j+1]}")
                if tested_number > largest_so_far:
                    largest_so_far = tested_number
    total_joltage += largest_so_far

print(total_joltage)