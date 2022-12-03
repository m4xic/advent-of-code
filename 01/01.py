with open('input', 'r') as fp:
    file = fp.read()

elves_calories = file.split('\n\n')
elves = []
for calories_string in elves_calories:
    calories_list = calories_string.split('\n')
    calories = 0
    while calories_list:
        calories += int(calories_list[-1])
        calories_list.pop()
    elves.append(calories)
print(elves)
print(max(elves))

top_3 = []
while len(top_3) < 3:
    biggest = max(elves)
    top_3.append(biggest)
    elves.remove(biggest)
print(top_3)
