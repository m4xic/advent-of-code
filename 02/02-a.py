with open("input", "r") as f:
    lines = f.readlines()

# The Elf would first like to know which games would have been possible
# if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

limits = {"red": 12, "green": 13, "blue": 14}
games = list(range(1, len(lines) + 1))

for line in lines:
    line = line.strip()
    game_id = int(line.split(":")[0].split(" ")[-1])
    print(game_id)
    rounds = line.split(":")[1].split(";")
    for this_round in rounds:
        for each_colour in this_round.split(","):
            num = int(each_colour.strip().split(" ")[0])
            colour = each_colour.strip().split(" ")[1]
            if num > limits[colour]:
                try:
                    games.remove(game_id)
                except:
                    print("already removed")

print(games)
print(sum(games))
