import os
bestandsnaam = "kluizen.txt"

#maak functie om het aantal kluizen op te vragen. Deze kan je later weer opvragen
def aantal_kluizen_vrij():
    if not os.path.exists(bestandsnaam):
        return 12  # Als het bestand niet bestaat, zijn alle kluizen beschikbaar
    else:
        with open(bestandsnaam, "r") as file:
            lines = file.readlines()
            return 12 - len(lines)
        #read hoeveel lijnen er zijn in het bestand. en doe dan 12- aantal lijnen voor hoeveel kluizen nog over zijn

#Def nieuwe kluis maakt een functie waarmee je een nieuwe kluis kan aanmaken. Deze functie kan je later weer oproepen
def nieuwe_kluis():
    kluisnummers = [i for i in range(1, 13)]

    if os.path.exists(bestandsnaam):
        with open(bestandsnaam, "r") as file:
            for line in file:
                kluisnummer = int(line.split(";")[0])
                if kluisnummer in kluisnummers:
                    kluisnummers.remove(kluisnummer)
            #De lijst updaten met welke kluizen er nog over zijn voor gebruik
            #leest eerst de file. met line.split[0] haalt hij het kluisnummer van elke kluis in de kluizen.txt
            #dan verwijdert ie alle nummers die in de tekst file en dan houd je dus de overgebleven dingen over waaruit je een kluis kan assignen

#checkt of kluisnummers leeg is
    if not kluisnummers:
        return -2  # Geen kluizen beschikbaar
    else:
        nieuwe_kluisnummer = kluisnummers[0]
        kluiscode = str(input("Voer een kluiscode in: (1234)"))
        if kluiscode.isdigit() and len(str(kluiscode)) == 4:
            #isdigit word hier gebruikt om te kijken of het ingevoerde getal een int is.
            with open(bestandsnaam, "a") as file:
                file.write(f"{nieuwe_kluisnummer};{kluiscode}\n")
                #schrijf het kluisnummer;met;een;kluiscode;weg
            return nieuwe_kluisnummer
        #return het kluisnummer om later te gebruiken
        else:
            return -1
        #kluiscode is niet correct




#met deze functie kan je een bestand openen. Deze functie kan je daardoor  later weer oproepen.
def kluis_openen():
    kluisnummer = str(input("Voer uw kluisnummer in: "))
    kluiscode = str(input("Voer uw kluiscode in: "))

    if os.path.exists(bestandsnaam):
        with open(bestandsnaam, "r") as file:
            for line in file:
                saved_kluisnummer, saved_kluiscode = map(str, line.strip().split(";"))
                #dit stored het eerste int van de file per lijn in saved_kluisnummer, en het 2e deel in saved_kluiscode.met de map functie zet deze lijst om  in ints
                if saved_kluisnummer == kluisnummer and saved_kluiscode == kluiscode:
                    #checkt of de opgegeven kluisnummer en kluiscode overeenkomen.
                    return True

    return False

def kluis_teruggeven():
    kluisnummer = str(input("Voer uw kluisnummer in: "))
    kluiscode = str(input("Voer uw kluiscode in: "))

    lines_to_keep = []  #maak een lijstje met de kluizen die je wilt bewawren
    found = False  #maak een var aan om aan te geven of de codes overeenkomen

    if os.path.exists(bestandsnaam):
        with open(bestandsnaam, "r") as file:
            for line in file:
                saved_kluisnummer, saved_kluiscode = map(str, line.strip().split(";"))

                if saved_kluisnummer == kluisnummer and saved_kluiscode == kluiscode:
                    found = True  # var om te controleren of de codes werken
                    continue  #deze lijn skipt hij in de loop omdat deze juist niet meer in het bestand wilt hebben
                else:
                    #voeg de lines toe die aan het bestand moeten toegevoegd
                    lines_to_keep.append(line)

        if found:
            # Schrijf de lines terug nadat je de combinatie hebt geverified
            with open(bestandsnaam, "w") as file:
                file.writelines(lines_to_keep)
            return True
        #boolean true terug geven als het is gelukt
        else:
            return False
        #boolean False terug geven als het niet is gelukt
    else:
        print("Het bestand is niet gevonden.")
        return False


valid = "false"
while valid == "false":
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis ")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")
    print("5: Afsluiten\n")
    function = input("Voer uw keuze in: (1/2/3/4/5) ")
    #hoofdmenu in een loop




    if function == "1":
        valid = "true"
        print(f"Aantal vrije kluizen: {aantal_kluizen_vrij()}\n")
        #print het aantal kluizen vrij in een fstring


    elif function == "2":
        valid = "true"
        resultaat = nieuwe_kluis()
        if resultaat == -2:
            print("Geen kluizen beschikbaar.")
        elif resultaat == -1:
            print("Je kluiscode moet precies 4 cijfers bevatten")
        else:
            print(f"Uw persoonlijke kluis is aangemaakt. Uw kluisnummer is: {resultaat}")
        #print de resultaten uit de define


    elif function == "3":
        valid = "true"
        if kluis_openen():
            print("Kluis geopend. (Wachtwoord goed)")
        else:
            print("Ongeldige combinatie van kluisnummer en code.")
        #print de waarden uit de define van kluis openen

    elif function == "4":
        valid = "true"
        teruggeven = kluis_teruggeven()
        if teruggeven:
            print("Kluis succesvol teruggegeven.")
        elif teruggeven == False:
            print("Ongeldige combinatie van kluisnummer en code.")
        else:
            print("Er is iets fout gegaan. Probeer het later opnieuw")
        #error code omdat het eerst nog wel eens fout ging met de boolean


    elif function == "5":
        print("U verlaat nu het programma...")
        break
    else:
        print("Ongeldige keuze (1/2/3/4)")
        valid = "false"
        loophoofdmenu = "false"
        ongeldige_keuze = "true"
        #loop vars instellen om te loopen


    loophoofdmenu = "true"
    while loophoofdmenu == "true":
        hoofdmenu = str(input("Wilt u terug naar het hoofdmenu? (ja/nee) ")).lower()
        print("")
        if hoofdmenu == "ja":
            valid = "false"
            loophoofdmenu = "false"
        elif hoofdmenu == "nee":
            valid = "true"
            print("U verlaat nu deze applicatie...")
            loophoofdmenu = "false"
            break
        else:
            loophoofdmenu = "true"
            #grote loop zodat sommige dingen breaken en sommige dingen juist nog een keer loopen
