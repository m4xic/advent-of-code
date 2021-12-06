class Lanternfish:
    def __init__(self, timer):
        self.timer = int(timer)

    def new_day(self):
        if self.timer == 0:
            self.timer = 6
            return 1
        else:
            self.timer -= 1
            return 0

fish_list = []

with open('06', 'r') as f: imported_fish = f.read().split(',')
for imported in imported_fish: fish_list.append(Lanternfish(imported))

for day in range(1, 81):
    fish_to_add = 0
    for fish in fish_list:
        fish_to_add += fish.new_day()
    for i in range(0, fish_to_add):
        fish_list.append(Lanternfish(8))
    print(f"End of day {day}: {len(fish_list)} fish")
