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

        print(ranges)
        print(letter + " " + string)

        status = [0,0]

        if string[int(ranges[0]) - 1] == letter:
            status[0] += 1
        if string[int(ranges[1]) - 1] == letter:
            status[1] += 1
        
        if status == [0,0] or status == [1,1]:
            no += 1
        else:
            yes += 1

    print(yes)
    print(no)