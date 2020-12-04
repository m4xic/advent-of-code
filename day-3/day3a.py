def do_extend_map(current_map):
    f = open('input', 'r')
    l = f.readlines()
    for i in range(0, len(current_map)):
        test = l[i].replace("\n", "")
        current_map[i] += test
    f.close()
    return current_map

def do_initial_map():
    f = open('input', 'r')
    l = f.readlines()
    initial_map = []
    for line in l:
        test = line.replace("\n", "")
        initial_map.append(test)
    f.close()
    return initial_map

def main():
    ride_map = do_initial_map()
    vert_position = 1
    horz_position = 3
    trees = 0
    while True:
        print("vert_position = " + str(vert_position) + ", horz_position = " + str(horz_position) + ", len(ride_map) = " + str(len(ride_map)) + ", len(ride_map[0]) = " + str(len(ride_map[0])))
        if vert_position > len(ride_map) - 1:
            break
        elif horz_position > len(ride_map[vert_position]) - 1:
            ride_map = do_extend_map(ride_map)
            continue
        else:
            if ride_map[vert_position][horz_position] == "#":
                print("I hit a tree at " + str(vert_position) + ", " + str(horz_position) + "!")
                trees += 1
            vert_position += 1
            horz_position += 3
    
    print(ride_map)
    print(trees)

main()