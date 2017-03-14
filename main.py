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

reader()
reader_v2()
