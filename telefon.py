class Timedates:
    def __init__(self, h, min, sec):
        self.sec = sec
        self.min = min
        self.h = h

    def __str__(self):
        return f"{self.sec} {self.min} {self.h}"

    def masodperc(self):
        return self.h*60*60+self.min*60+self.sec


file = open("hivas.txt", "rt", encoding="utf-8")
starttimedates = []
endtimedates = []

for row in file:
    i = row.strip().split(" ")
    starttimedates.append(Timedates(i[0], i[1], i[2]))
    endtimedates.append(Timedates(i[3], i[4], i[5]))
file.close()


