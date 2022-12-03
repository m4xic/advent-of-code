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
for rucksack in rucksacks:
    rucksack = rucksack.strip()
    slicer = len(rucksack)//2
    comp_one, comp_two = rucksack[:slicer], rucksack[slicer:]
    for letter in comp_one:
        print(letter)
        if letter in comp_two:
            print('found letter', letter, comp_one, comp_two)
            priorities += get_prio(letter)
            break
print(priorities)
