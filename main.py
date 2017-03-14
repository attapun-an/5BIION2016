def reader():
    player_name = []
    file = open("NAMES.txt", "r")
    for i in range(1, 9):
        player_name.append(file.readline())
    print(player_name)
    file.close()


def reader_v2():
    player_name = []
    file = open("NAMES.txt", "r").read().splitlines()
    for line in file:
        player_name.append(line)
    print(player_name)


def reader_v3():
    player_name = []
    file = open("NAMES.txt", "r")
    read = file.read()
    separated = read.splitlines()
    player_name.append(separated)
    print(player_name)


reader()
reader_v2()
reader_v3()
