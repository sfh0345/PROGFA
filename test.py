import os

# Bestandsnaam om de kluizen bij te houden
bestandsnaam = "fa_kluizen.txt"

def development_code():
    print("1. Toon het aantal vrije kluizen")
    print("2. Huur een nieuwe kluis")
    print("3. Open een kluis")
    print("4. Geef een kluis terug")

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

    if not kluisnummers:
        return -2  # Geen kluizen beschikbaar
    else:
        nieuwe_kluisnummer = kluisnummers[0]
        kluiscode = input("Voer een kluiscode in: ")

        # Voeg de nieuwe kluis toe aan het bestand
        with open(bestandsnaam, "a") as file:
            file.write(f"{nieuwe_kluisnummer};{kluiscode}\n")

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

# Test de functies
def main():
    while True:
        development_code()
        keuze = int(input("Voer uw keuze in: "))

        if keuze == 1:
            print(f"Aantal vrije kluizen: {aantal_kluizen_vrij()}")
        elif keuze == 2:
            resultaat = nieuwe_kluis()
            if resultaat == -2:
                print("Geen kluizen beschikbaar.")
            else:
                print(f"U heeft kluisnummer: {resultaat}")
        elif keuze == 3:
            if kluis_openen():
                print("Kluis geopend.")
            else:
                print("Ongeldige combinatie van kluisnummer en code.")
        elif keuze == 4:
            if kluis_teruggeven():
                print("Kluis succesvol teruggegeven.")
            else:
                print("Ongeldige combinatie van kluisnummer en code.")
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

        doorgaan = input("Wilt u nog een actie uitvoeren? (ja/nee): ").lower()
        if doorgaan != 'ja':
            break

if __name__ == "__main__":
    main()
