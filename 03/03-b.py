import string


lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)


def get_prio(letter):
    if letter in lower:
        return lower.index(letter) + 1
    else:
        return upper.index(letter) + 27


with open('input', 'r') as fp:
    rucksacks = fp.readlines()

priorities = 0
for i in range(len(rucksacks)//3):
    group = rucksacks[3*i:3*i+3]
    for j in range(3):
        group[j] = group[j].strip()
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            print('badge found', letter, group)
            priorities += get_prio(letter)
            break
print(priorities)
