with open('input', 'r') as f:
    f = f.readlines()
    yes = 0
    no = 0
    for line in f:
        line = line.rstrip()
        components = line.split(" ")
        ranges = components[0].split("-")
        letter = components[1][0]
        string = components[2]

        if string.count(letter) in range(int(ranges[0]), int(ranges[1]) + 1):
            yes += 1
        else:
            no += 1
    print(yes)
    print(no)