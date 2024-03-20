class Timedates:
    def __init__(self, h, min, sec):
        self.sec = int(sec)
        self.min = int(min)
        self.h = int(h)

    def __str__(self):
        return f"{self.h} {self.min} {self.sec}"

    def masodperc(self):
        return self.h*60*60+self.min*60+self.sec


file = open("hivas.txt", "rt", encoding="utf-8")
infile = open("sikeres.txt", "wt", encoding="utf-8")
starttimedates = []
endtimedates = []
sixtask = []
seven = []
stat = {}
bigest = count = bigcount = talker = waiting = x = switch = counter = switchtwo = 0
start = int(8*60*60)
end = int(12*60*60)

for row in file:
    i = row.strip().split(" ")
    starttimedates.append(Timedates(i[0], i[1], i[2]))
    endtimedates.append(Timedates(i[3], i[4], i[5]))
file.close()

for i in starttimedates:
    if i.h in stat.keys():
        stat[i.h] += 1
    else:
        stat[i.h] = 1

print("3. feladat")
for k,v in stat.items():
    print(f"{k} ora {v} hivas")

while start > x:
    x = input("\n5. feladat \nAdjon meg egy idopontot! (ora perc masodprec) ")
    x = x.strip().split(" ")
    x = int(x[0]) * 60 * 60 + int(x[1]) * 60 + int(x[2])
    while end < x:
        x = input("\n5. feladat \nAdjon meg egy idopontot! (ora perc masodprec) ")
        x = x.strip().split(" ")
        x = int(x[0])*60*60 + int(x[1])*60 + int(x[2])


for i in range(len(starttimedates)):
    count += 1
    if bigest < int(endtimedates[i].masodperc()) - int(starttimedates[i].masodperc()):
        bigest = int(endtimedates[i].masodperc()) - int(starttimedates[i].masodperc())
        bigcount = count

    if x < starttimedates[i].masodperc() and switch == 0 and x < endtimedates[i].masodperc():
        print(f"A varakozok szama: {waiting} a beszelo a {talker}. hivo")
        switch = 1


    if start < endtimedates[i].masodperc() and starttimedates[i].masodperc() < end:
        start = endtimedates[i].masodperc()
        talker = count
        waiting = 0
        sixtask.append(start)
        seven.append(endtimedates[i])
        counter = starttimedates[i].masodperc()
        if switchtwo == 0 :
            infile.write(f"{talker} 8 0 0 {endtimedates[i]} \n")
            switchtwo = 1
        else:
            infile.write(f"{talker} {seven[-2]} {endtimedates[i]} \n")
    else:
        waiting += 1





print(f"\n4. feladat \nA leghosszabb ideig vonalban levo hivo {bigcount}. sorban szerepel, a hivas hossza: {bigest} masodperc.")
print(f"\n6. feladat \nAz utolso telefonalo adatai a(z) {talker}. sorban vannak, {sixtask[-2] - counter} masodpercig vart")
