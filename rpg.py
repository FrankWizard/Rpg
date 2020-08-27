import time, random

print("Ahoj vítej v editoru tvé postavy")

time.sleep(0.5)

print("Nejdříve si prosím zvol rasu")

time.sleep(0.5)

print("1) Elf")
print("2) Člověk")
print("3) Trpaslík")

sila = 0
charisma = 0
agility = 0

hp = 100
zlato = 50

Rasa = int(input())

if Rasa == 1:

    agility = agility + 10
    sila = sila + 8
    charisma = charisma + 4

    print("Zvolis jsi si Elfa jako svoji rasu")
    print("Toto jsou tvé schopnosti : ", charisma , "charisma", agility , "agility", sila, "síly")

if Rasa == 2:

    agility = agility +6
    sila = sila + 6
    charisma = charisma + 8

    print("Zvolis jsi si Člověka jako svoji rasu")
    print("Toto jsou tvé schopnosti : ", charisma , "charisma", agility , "agility", sila, "síly")

if Rasa ==3:

    agility = agility + 3
    sila = sila + 10
    charisma = charisma + 3

    print("Zvolis jsi si Trpaslíka jako svoji rasu")
    print("Toto jsou tvé schopnosti : ", charisma , "charisma", agility , "agility", sila, "síly")

time.sleep(0.4)

print("Teď si prosím vyber svoji classu")

time.sleep(0.4)

print("1) Mage")
print("2) Warrior")
print("3) Archer")

Class = int(input())

if Class == 1:

    agility = agility + 2
    sila = sila + 4
    charisma = charisma - 2

    print("Jako svojí classu jsi si vybral Mage")

    print("Toto jsou tvé schopnosti : ", charisma , "charisma", agility , "agility", sila, "síly")

if Class == 2:

    agility = agility -2
    sila = sila + 6
    charisma = charisma + 3

    print("Jako svojí classu jsi si vybral Warriora")

    print("Toto jsou tvé schopnosti : ", charisma , "charisma", agility , "agility", sila, "síly")

if Class == 3:

    agility = agility + 6
    sila = sila + 2
    charisma = charisma - 1

    print("Jako svojí classu jsi si vybral Archera")

    print("Toto jsou tvé schopnosti : ", charisma , "charisma", agility , "agility", sila, "síly")

print("Ahoj ještě ti musím nějak říkat, jak bych tě měl oslovovat?")

name = input()

print("Ahoj", name , "Objevil jsi se ve vesnici")

time.sleep(0.2)

print("Co by si chtěl dělat?")

time.sleep(0.2)

print("1) Najít si práci")
print("2) Porozhlédnout se")
print("3) Jít pryč")




vesnice = int(input())

while vesnice == 1:

    print("Jakou práci si vybereš?")

    time.sleep(0.5)

    print("1) Barman")
    print("2) Prodavač")
    print("3) Dřevorubec")

    prace = int(input())

    if prace == 1:

        luck = random.randint(1,100)

        hospodský = random.randint(55,75)

        time.sleep(0.1)

        print("Přišel jsi do místního baru a šel jsi rovnou za hospodským že hledáš práci")

        time.sleep(0.1)

        print("Hospodský tebou není přesvědčený... Potřebuješ", hospodský , "charisma a trochu štěstí, hoď si kosktou")

        time.sleep(0.1)

        input("Stisknutim Enter hodis kostku")

        time.sleep(0.1)

        if luck > 49:
            dice = random.randint(8,24)
            print("Na kostce jsi hodil: ", dice,)
        if luck < 49:
            dice = random.randint(1,24)
            print("Na kostce jsi hodil: ", dice,)

        print("Tvoje charisma nyni je: ", charisma*dice)

        charisma = charisma*dice


        if charisma > hospodský:

           zlato = zlato + 25

           print("Gratuluji hospodský tě přijal do práce jako barmana")
           print("Ziskal si 25 zlaťáků teď máš", zlato , "zlaťáků")

        else:
            print("Bohužel hospodský tě nepřijal do práce")

    if prace == 69:

        charisma = charisma + 50

        zlato = zlato + 150

        print("Gratuluji", name , "jsi zaměstnán jako striptér")

        print("Vydělal jsi si 150 zlaťáků teď máš", zlato,"zlaťáků")

        print("Tvoje charisma se také zvedlo o 50 bodů, tvé charisma je teď : ", charisma)


    if prace == 2:

        luck = random.randint(1,100)

        time.sleep(0.1)

        print("Přišel jsi do místního obchodu a šel jsi rovnou za vedoucím že hledáš práci")

        time.sleep(0.1)

        print("Vedoucí tebou není přesvědčený... Potřebuješ 65 charisma a trochu štěstí, hoď si kosktou")

        time.sleep(0.1)

        input("Stisknutim Enter hodis kostku")

        time.sleep(0.1)

        if luck > 49:
            dice = random.randint(8,24)
            print("Na kostce jsi hodil: ", dice,)
        if luck < 49:
            dice = random.randint(1,24)
            print("Na kostce jsi hodil: ", dice,)

        print("Tvoje charisma nyni je: ", charisma*dice)

        charisma = charisma*dice


        if charisma > 66:

           zlato = zlato + 30

           print("Gratuluji vedoucí prodeje tě přijal do práce jako prodavače")
           print("Ziskal si 30 zlaťáků teď máš", zlato , "zlaťáků")

        else:
            print("Bohužel hospodský tě nepřijal do práce")

    if prace == 3:

        luck = random.randint(1,100)
        accuracy = random.randint(1,50)

        time.sleep(0.1)

        print("Přišel jsi do místní pily a šel jsi rovnou za vedoucím že hledáš práci")

        time.sleep(0.1)

        print("Vedoucí tebou není přesvědčený... Potřebuješ 45 sily.")

        print("Kolik % sve sily chces pouzit? 0% az 100%")
        power = int(input())

        time.sleep(0.1)

        input("Stisknutim Enter seknes sekerou")

        time.sleep(0.1)

        if luck > 49:

            power = power - accuracy
            print("Sekl si do stromu tvoje presnost byla: ", power)

            if power > 59:
                print("Vedouci je presvedcen a bere te jako drevorubce")
                zlato = zlato + 30
                print("Získal jsi 30 zlaťáků, teď máš ",zlato,"zlata")

        if luck < 50:

            power = power - accuracy
            print("Sekl si do stromu tvoje presnost byla: ", power)

            if power < 60:

                print("Vedouci je presvedcen a bere te jako drevorubce")
                zlato = zlato + 15
                print("Ted mas: ",zlato,"zlata")

print("1) Najít si práci")
print("2) Porozhlédnout se")
print("3) Jít pryč")



vesnice = int(input())



if vesnice == 2:

    print("Rozhodl jsi se prozkoumat vesnici a našel jsi pár věcí... Kam chceš jít?")

    print("1) Obchod")
    print("2) Hospoda")
    print("3) Král")

    explore = int(input())

    if explore == 1:


        print("Rozhodl jsi se jít do obchodu jsou zde 3 sekce kde chceš nakupovat?")

        print("1) Zbraně")
        print("2) Elixíry")
        print("3) Training")
        print("4) Chci odejít")

        sekce = int(input())



        while sekce != 4:




            if sekce == 1:

                print("Na výběr jsou zde 3 zbraně jakou si chceš si koupit?")

                print("1) Meč (110 zlaťáků)")
                print("2) Sekyra (130 zlaťáků)")
                print("3) Luk (100 zlaťáků)")
                print("4) Chci odejít")

                vyber = int(input())

                if vyber == 1:
                    if  zlato > 110:
                        zlato = zlato - 110

                        print("Gratuluji úspešně sis koupil meč, teď máš : ", zlato , "zlata")

                    elif zlato < 110:
                        print("Máš málo zlata na tuto zbraň potřebuješ 110 zlaťáků, máš :", zlato , "zlata")



                if vyber == 2:
                    if  zlato > 130:
                        zlato = zlato - 130

                        print("Gratuluji úspešně sis sekeru, teď máš : ", zlato , "zlata")

                    elif zlato < 130:
                        print("Máš málo zlata na tuto zbraň potřebuješ 130 zlaťáků, máš :", zlato , "zlata")


                if vyber == 3:
                    if  zlato > 100:
                        zlato = zlato - 100

                        print("Gratuluji úspešně sis luk, teď máš : ", zlato , "zlata")

                    elif zlato < 100:
                        print("Máš málo zlata na tuto zbraň potřebuješ 100 zlaťáků, máš :", zlato , "zlata")






                print("1) Zbraně")
                print("2) Elixíry")
                print("3) Training")
                print("4) Chci odejít")

                sekce = int(input())


        print("Kam chceš jít?")
        print("1) Obchod")
        print("2) Hospoda")
        print("3) Král")
        print("4) Vesnice - Náměstí")

        explore = int(input())

        if   explore == 4:

          print("1) Najít si práci")
          print("2) Porozhlédnout se")
          print("3) Jít pryč")

          vesnice = int(input())















        input("press enter")



        

               
