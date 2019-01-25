# Last edited: 24-1-2019 GD Vis
# Source bot: https://maker.pro/raspberry-pi/projects/how-to-create-a-telegram-bot-with-a-raspberry-pi
import telepot
from telepot.loop import MessageLoop
from time import sleep
import pymysql
import datetime


# Deze functie checkt de inputs van de gebruikers en geeft daarop informatie terug aan de gebruiker
def brain(message):
    chat_id = message["chat"]["id"]
    # De try en except is aanwezig zodat als een gebruiker iets anders stuurt dan tekst de gebruiker een foutmelding
    # krijgt ipv de code die een foutmelding geeft
    try:
        command = message['text']
        user = message["chat"]["first_name"]
        user_id = message["chat"]["id"]

        # Hierdoor kun je vanaf de server zien welke gebruiker welke opdracht aanvraagt
        print("Received:")
        print("{} | From: {}, id: {}".format(command, user, user_id))

        to_log = "{} | From: {}".format(command, user)
        logger(to_log)

        # De opdrachte  checken of die bestaat en dan uitvoeren
        if command == "/info":
            bot.sendMessage(chat_id, str("Hallo {}. Ik ben de Trashman ik kan data opvragen over de prullenbakken voor jou. "
                                         "Hierdoor wordt het afval in de wijk Ravensweerd optijd geleegd. "
                                         "https://media.giphy.com/media/2w6I6nCyf5rmy5SHBy/giphy.gif".format(user)))

        elif command == "/help":
            bot.sendMessage(chat_id, str("Functies: /containers,\n/check[container ID], /werk, /extra"))

        elif command == "/extra":
            bot.sendMessage(chat_id, str("Extra functies die ik kan uitvoeren:\n /info, /music, /versie"))

        elif command == "/versie":
            bot.sendMessage(chat_id, str("Versie: 1.06, Gemaakt door: Hei5enberg, https://github.com/Hei5enberg."))

        elif command == "/music":
            bot.sendMessage(chat_id, str("Mijn favoriete liedje Garbage: ¯\_(ツ)_/¯\n"
                                         "https://soundcloud.com/rampantgoddess/garbage-tyler-the-creator"))

        # Deze opdracht geeft aan de gebruiker de ID's van de containers terug.
        elif command == "/containers":
            try:
                message = database_requests(0, "empty")

                containers = ""
                for i in range(0, len(message)):
                    if i == len(message) - 1:
                        containers += "{}.".format(message[i])
                    else:
                        containers += "{}, ".format(message[i])

                bot.sendMessage(chat_id, str("Alle container ID's: {}").format(containers))
            except pymysql.err.OperationalError:
                bot.sendMessage(chat_id, str("Geen connectie met de database. Excuses voor het ongemak"))
                print("*** NO CONNECTION WITH DATABASE ***")

        # Met deze command kan de gebruiker de informatie die de database van de container heeft checken en terugsturen aan de gebruiker
        elif command.startswith("/check "):
            try:
                try:
                    check = database_requests(1, command[7:])
                    if check[0]:
                        bot.sendMessage(chat_id, str("Container data gevonden!"))

                        formatted_message = "Container: {} | Percentage vol: {}% | Afvalhoogte: {}cm".format(check[1][0], check[1][1], check[1][2])
                        bot.sendMessage(chat_id, str(formatted_message))
                except TypeError:
                    bot.sendMessage(chat_id, str("Container niet gevonden. Probeer opnieuw: /check [container ID]"))
            except pymysql.err.OperationalError:
                bot.sendMessage(chat_id, str("Geen connectie met de database. Excuses voor het ongemak"))
                print("*** NO CONNECTION WITH DATABASE ***")

        elif command == "/check":
            bot.sendMessage(chat_id, str("Voer /check [container ID] anders werk ik niet"))

        elif command == "/werk":
            try:
                check = database_requests(2, "empty")
                message = "Deze containers moeten geleegd worden: "

                for i in range(0, len(check)):
                    if i == len(check) - 1:
                        insert = "{}: {}%".format(check[i][0], check[i][1])
                        message += insert
                    else:
                        insert = "{}: {}% | ".format(check[i][0], check[i][1])
                        message += insert

                bot.sendMessage(chat_id, str(message))
            except pymysql.err.OperationalError:
                bot.sendMessage(chat_id, str("Geen connectie met de database. Excuses voor het ongemak"))
                print("*** NO CONNECTION WITH DATABASE ***")

        # Als de opdracht die de gebruiker stuurt nergens mee overeenkomt krijgt hij/zij een melding
        else:
            bot.sendMessage(chat_id, str("Opdracht niet gevonden probeer /help"))

    # De foutmelding die de gebruiker krijgt als hij/zij iets anders stuurt dan tekst
    except KeyError:
        bot.sendMessage(chat_id, str("Ik snap niks van dit bericht ik werk alleen maar met tekst :)"))


# Deze functie haalt de informatie uit de database op en stopt dit in een lijst die database_requests kan gebruiken
def sql_checker():
    # Lijst waar alle informatie van de container in wordt opgeslagen
    container_data = []

    # Connectie data
    conn = pymysql.connect(
        host='10.0.0.210',
        user='root',
        passwd='Beukenlaan81',
        db='vuilcontainerproject',
        autocommit=True
    )
    cursor = conn.cursor()

    cursor.execute(
        "select * from vuilcontainerproject.vuilcontainerStatus group by FK_vuilcontainerID order by LENGTH(FK_vuilcontainerID), FK_vuilcontainerID;")

    rows = cursor.fetchall()

    for row in rows:
        templist = [row[0], row[1], row[2], float(row[3])]
        container_data.append(templist)

    conn.close()
    return(container_data)


# Deze functie geeft de informatie terug die relevant is voor de gebruiker
def database_requests(mode, modifier):
    packet = sql_checker()

    # Mode 0 alleen de ID's van de containers terug
    if mode == 0:
        return_packet = []
        for i in range(0, len(packet)):
            return_packet.append(packet[i][0])
        return return_packet

    # Mode 1 checkt of de container die gecheckt moet worden bestaat en zo ja dan wordt de informatie teruggestuurd.
    elif mode == 1:
        container_IDs = []
        for i in range(0, len(packet)):
            container_IDs.append(packet[i][0])

        counter = 0
        while counter < len(container_IDs):
            if modifier == container_IDs[counter]:
                return [True, packet[counter]]
            else:
                counter += 1

    # Checkt welke containers 90% vol zijn
    elif mode == 2:
        return_packet = []
        for i in range(0, len(packet)):
            current = packet[i][1]
            if current >= 95:
                return_packet.append([packet[i][0],current])

        return return_packet


# Functie die chat ontvangsten opslaat waarschijnlijk beetje tegen AVG ¯\_(ツ)_/¯
def logger(message):
    file = open("chat_log.txt", "a+")

    today = datetime.datetime.today()
    timeData = today.strftime("%H:%M:%S | %d %b %y")

    file.write("{} at {}\n".format(message, timeData))
    file.close()


# Setup van de bot
try:
    bot = telepot.Bot("Si Sa Secret")
    print("Checking connection: ")
    print(bot.getMe())

    MessageLoop(bot, brain).run_as_thread()
    print("Listening.....")
except:
    print("*** ERROR STARTING BOT ***")

# While loop zodat de bot aanblijft
while 1:
    sleep(10)
