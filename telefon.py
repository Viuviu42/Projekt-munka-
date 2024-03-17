file = open("hivas.txt", "rt", encoding="utf-8")
timedates = []

for row in file:
    i = row.strip().split(" ")
    timedates.append(i)
file.close()


