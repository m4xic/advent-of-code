with open('06', 'r') as f: imported_fish = f.read().split(',')
current_fish = []

fish_count = {
    0: int(imported_fish.count('0')),
    1: int(imported_fish.count('1')),
    2: int(imported_fish.count('2')),
    3: int(imported_fish.count('3')),
    4: int(imported_fish.count('4')),
    5: int(imported_fish.count('5')),
    6: int(imported_fish.count('6')),
    7: int(imported_fish.count('7')),
    8: int(imported_fish.count('8'))
}
print(fish_count)
day = 1
while day < 257:
    print(f"** Starting day {day}")
    temp = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for i in range(1, 9):
        temp[i-1] = fish_count[i]
    temp[6] += fish_count[0]
    temp[8] += fish_count[0]
    print(sum(temp.values()))
    fish_count = temp
    day += 1
