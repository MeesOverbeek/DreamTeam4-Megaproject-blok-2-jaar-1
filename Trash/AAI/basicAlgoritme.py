# Last updated: 18-1-2019 by Gijs Vis
# Simpel algoritme voor het bepalen van de optimale tijd om de prullenbakken te legen

import random
import csv
import datetime

# Deze functie zal willekeurige data creeëren binnen een bepaalde range.
# De data is gebaseerd op het feit dat er dagen zijn waar er meer afval gedumpt wordt.
# Dit omdat wij geen echte data hebben en dit de makkelijkste manier is om zelf veel data te creeëren


# Drukke dagen dinsdag en vrijdag maximale toename 40%. Rustige dagen maandag,donderdag,zondag maximale toename 15%.
# Normale dagen: woensdag en zaterdag maximale toename 30%
def data_randomizer():
    week = ["mon", "tue", "wen", "thu", "fri", "sat", "sun"]

    # Rustige dagen
    for i in range(0,3):
        increase = random.randrange(0, 16)
        if i == 0:
            week[week.index("mon")] = increase
        elif i == 1:
            week[week.index("thu")] = increase
        else:
            week[week.index("sun")] = increase

    # Normale dagen
    for i in range(0,2):
        increase = random.randrange(0, 31)
        if i == 0:
            week[week.index("wen")] = increase
        elif i == 1:
            week[week.index("sat")] = increase

    # Drukke dagen
    for i in range(0,2):
        increase = random.randrange(0, 41)
        if i == 0:
            week[week.index("tue")] = increase
        elif i == 1:
            week[week.index("fri")] = increase

    return(week)


# Functie die een packet een x aantal weken aan data maakt
def packet_creator():
    packet = []
    for i in range(0, 100000):
        week_list = data_randomizer()
        packet.append(week_list)

    return packet


# Functie die checkt of de afval containers vol zijn en wanneer
def checker(week):
    counter = 0
    last = 0
    while counter < 7:
        last = last + week[counter]
        if last >= 100:
            message = [counter, True, last]
            counter -= counter
            return message
        elif counter == 6:
            counter -= counter
            return "False"

        counter += 1


# Dit is het "algoritme" dat zal bepalen welke dag de prullenbak gemiddeld vol raakt en op welk percentage
def algoritme():
    packet = packet_creator()
    results = []
    week_days = []
    full_per = []

    for i in range(0, len(packet)):
        result = checker(packet[i], i + 1)
        results.append(result)

    for i in range(0, len(results)):
        try:
            to_remove = results.index("False")
            results.pop(to_remove)
        except ValueError:
            pass

    for i in range(0, len(results)):
        to_add = results[i][0]
        add_per = results[i][2]
        week_days.append(to_add)
        full_per.append(add_per)

    avg_day = sum(week_days) / len(week_days)
    avg_per = sum(full_per) / len(full_per)

    print("De optimale dag om het afval te legen is dag: {} | Met een gemiddelde vulling van {}%".format(round(avg_day), round(avg_per)))
    return_message = "De optimale dag om het afval te legen is dag: {} | Met een gemiddelde vulling van {}%".format(round(avg_day), round(avg_per))
    time = datetime.datetime.now().strftime("%d-%m-%y | %H:%M:%S")

    csvFile = "data.csv"
    with open(csvFile, 'a') as dataCSV:
        writer = csv.writer(dataCSV)
        message =["Data toegevoegd: {} \n{}\n".format(time, return_message)]
        writer.writerow(message)
