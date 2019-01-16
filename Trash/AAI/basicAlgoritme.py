# 16-1-2019 Gijs Vis
# Poging tot algoritme voor het bepalen van de optimale tijd om de prullenbakken te legen
# Neemt het aantal dagen totdat de prullenbak 100% vol zijn en berekent hoe lang het gemiddeld duurt per 5% opvulling
# [[10,20,30,40,56,80,90],[5,30,37,66,70,90,100],[44,37,70,76,88,95,100],[7,15,60,63,67,75,88]]


def average(values):
    valueLen = len(values)
    # Gemiddelde berekenen van alle data
    calculation1 = sum(values) / valueLen
    # Berekent hoe lang het gemiddeld duurt voor het vullen per 5%
    calculation2 = (calculation1 / 100) * 5
    print("Het duurt {} dag(en) per 5% opvulling".format(calculation2))


def average_day(values):
    valuesLen = len(values)

    mon = []
    tue = []
    wen = []
    thu = []
    fri = []
    sat = []
    sun = []

    for i in range(0, valuesLen):
        mon.append(values[i][0])
        tue.append(values[i][1])
        wen.append(values[i][2])
        thu.append(values[i][3])
        fri.append(values[i][4])
        sat.append(values[i][5])
        sun.append(values[i][6])

    avgMon = sum(mon) / len(mon)
    avgTue = sum(tue) / len(tue)
    avgWen = sum(wen) / len(wen)
    avgThu = sum(thu) / len(thu)
    avgFri = sum(fri) / len(fri)
    avgSat = sum(sat) / len(sat)
    avgSun = sum(sun) / len(sun)

    incTue = round(avgTue - avgMon)
    incWen = round(avgWen - avgTue)
    incThu = round(avgThu - avgWen)
    incFri = round(avgFri - avgThu)
    incSat = round(avgSat - avgFri)
    incSun = round(avgSun - avgSat)

    print("Average increases per day")
    print("Mon | Tue | Wen | Thu | Fri | Sat | Sun")
    print("{:2}% | {:2}% | {:2}% | {:2}% | {:2}% | {:2}% | {:2}%".format(round(avgMon), incTue, incWen, incThu, incFri, incSat, incSun))

