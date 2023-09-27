import os
bestandsnaam = "kluizen.txt"


def aantal_kluizen_vrij():
    if not os.path.exists(bestandsnaam):
        return 12  # Als het bestand niet bestaat, zijn alle kluizen beschikbaar
    else:
        with open(bestandsnaam, "r") as file:
            lines = file.readlines()
            return 12 - len(lines)


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

    if not kluisnummers:
        return -2  # Geen kluizen beschikbaar
    else:
        nieuwe_kluisnummer = kluisnummers[0]
        kluiscode = input("Voer een kluiscode in: ")

        # Voeg de nieuwe kluis toe aan het bestand
        with open(bestandsnaam, "a") as file:
            file.write(f"{nieuwe_kluisnummer};{kluiscode}")

        return nieuwe_kluisnummer




def kluis_openen():
    kluisnummer = int(input("Voer uw kluisnummer in: "))
    kluiscode = input("Voer uw kluiscode in: ")

    if os.path.exists(bestandsnaam):
        with open(bestandsnaam, "r") as file:
            for line in file:
                saved_kluisnummer, saved_kluiscode = map(int, line.strip().split(";"))
                if saved_kluisnummer == kluisnummer and saved_kluiscode == kluiscode:
                    return True

    return False

def kluis_teruggeven():
    kluisnummer = int(input("Voer uw kluisnummer in: "))
    kluiscode = input("Voer uw kluiscode in: ")

    lines_to_keep = []

    if os.path.exists(bestandsnaam):
        with open(bestandsnaam, "r") as file:
            for line in file:
                saved_kluisnummer, saved_kluiscode = map(int, line.strip().split(";"))
                if saved_kluisnummer == kluisnummer and saved_kluiscode == kluiscode:
                    continue  # Deze kluis wordt teruggegeven, dus niet bewaren in de nieuwe lijst
                else:
                    lines_to_keep.append(line)

    # Schrijf de bijgewerkte lijst met kluizen naar het bestand
    with open(bestandsnaam, "w") as file:
        file.writelines(lines_to_keep)

    return True



valid = "false"
while valid == "false":
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis ")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")
    print("5: Afsluiten\n")
    function = input("Voer uw keuze in: (1/2/3/4/5) ")




    if function == "1":
        valid = "true"
        print(f"Aantal vrije kluizen: {aantal_kluizen_vrij()}\n")




    elif function == "2":
        valid = "true"
        resultaat = nieuwe_kluis()
        if resultaat == -2:
            print("Geen kluizen beschikbaar.")
        else:
            print(f"Uw persoonlijke kluis is aangemaakt. Uw kluisnummer is: {resultaat}")




    elif function == "3":
        print("Functie 3:")
        valid = "true"




    elif function == "4":
        print("Functie 4:")
        valid = "true"
    elif function == "5":
        print("U verlaat nu het programma...")
        break
    else:
        print("Ongeldige keuze (1/2/3/4)")
        valid = "false"
        loophoofdmenu = "false"
        ongeldige_keuze = "true"


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


