PlayerName = []
file = open("NAMES.txt", "r")
for i in range(1, 9):
    PlayerName.append(file.readline())
print(PlayerName)
