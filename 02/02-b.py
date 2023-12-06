with open("input", "r") as f:
    lines = f.readlines()

# The Elf would first like to know which games would have been possible
# if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

powers = []

for line in lines:
    line = line.strip()
    game_id = int(line.split(":")[0].split(" ")[-1])
    minimums = {"red": 0, "green": 0, "blue": 0}
    rounds = line.split(":")[1].split(";")
    for this_round in rounds:
        for each_colour in this_round.split(","):
            num = int(each_colour.strip().split(" ")[0])
            colour = each_colour.strip().split(" ")[1]
            if num > minimums[colour]:
                minimums[colour] = num
    powers.append(minimums["red"] * minimums["green"] * minimums["blue"])

print(sum(powers))
