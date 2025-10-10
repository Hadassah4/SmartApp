def aantal_dagen(inputFile):
    try:
        with open(inputFile, 'r') as f:
            lines = f.readlines()
        return len(lines) - 1
    except FileNotFoundError:
        print("Fout: invoerbestand niet gevonden.")
        return 0


def auto_bereken(inputFile, outputFile):
   try:
        with open(inputFile, 'r') as f:
            lines = f.readlines()[1:]

        results = []
        for line in lines:
            if not line.strip():
                continue
            date, numPeople, setpoint, tempOutside, precip = line.strip().split()
            numPeople = int(numPeople)
            setpoint = float(setpoint)
            tempOutside = float(tempOutside)
            precip = float(precip)

            # Berekeningen
            temp_diff = setpoint - tempOutside
            if temp_diff >= 20:
                cv = 100
            elif temp_diff >= 10:
                cv = 50
            else:
                cv = 0

            ventilatie = min(numPeople + 1, 4)
            bewatering = True if precip < 3 else False

            results.append(f"{date};{cv};{ventilatie};{bewatering}")

        #resultaten -> uitvoerbestand
        with open(outputFile, 'w') as f:
            for line in results:
                f.write(line + "\n")

        print(f"Automatische berekening uitgevoerd. Uitvoer opgeslagen in '{outputFile}'.")
   except FileNotFoundError:
        print("Fout: invoerbestand niet gevonden.")
   except Exception as e:
        print("Er is een fout opgetreden bij het berekenen:", e)


def overwrite_settings(outputFile):
    try:
        with open(outputFile, 'r') as f:
            lines = f.readlines()

        if not lines:
            print("Uitvoerbestand is leeg.")
            return -1

        date_input = input("Voer de datum in (bijv. 08-10-2024): ").strip()
        found = False

        for i, line in enumerate(lines):
            parts = line.strip().split(";")
            if parts[0] == date_input:
                found = True
                print(f"Huidige waarden: CV={parts[1]}, Ventilatie={parts[2]}, Bewatering={parts[3]}")
                systeem = input("Kies systeem (1=CV ketel, 2=Ventilatie, 3=Bewatering): ").strip()

                # CV-ketel
                if systeem == "1":
                    try:
                        waarde = int(input("Nieuwe waarde voor CV (0-100): "))
                        if 0 <= waarde <= 100:
                            parts[1] = str(waarde)
                        else:
                            print("Ongeldige waarde.")
                            return -3
                    except ValueError:
                        print("Ongeldige invoer.")
                        return -3

                # Ventilatie
                elif systeem == "2":
                    try:
                        waarde = int(input("Nieuwe waarde voor Ventilatie (0-4): "))
                        if 0 <= waarde <= 4:
                            parts[2] = str(waarde)
                        else:
                            print("Ongeldige waarde.")
                            return -3
                    except ValueError:
                        print("Ongeldige invoer.")
                        return -3

                # Bewatering
                elif systeem == "3":
                    waarde = input("Nieuwe waarde voor Bewatering (0=uit, 1=aan): ").strip()
                    if waarde in ["0", "1"]:
                        parts[3] = "True" if waarde == "1" else "False"
                    else:
                        print("Ongeldige waarde.")
                        return -3
                else:
                    print("Ongeldig systeem gekozen.")
                    return -3

                # Update regel
                lines[i] = ";".join(parts) + "\n"
                print(f"Waarden voor {date_input} succesvol aangepast.")
                break

        if not found:
            print("Datum niet gevonden.")
            return -1

        # regels -> bestand
        with open(outputFile, 'w') as f:
            f.writelines(lines)

        return 0

    except FileNotFoundError:
        print("Fout: uitvoerbestand niet gevonden.")
        return -1
    except Exception as e:
        print("Er is een fout opgetreden:", e)
        return -3


def smart_app_controller():
    print("=== SMART HOME CONTROLLER ===")
    inputFile = input("Voer de naam van het invoerbestand in (bijv. input.txt): ").strip()
    outputFile = "output.txt"

    while True:
        print("\nMenu:")
        print("1. Toon aantal dagen in invoerbestand")
        print("2. Bereken automatisch alle actuatoren en schrijf uitvoerbestand")
        print("3. Overschrijf een waarde in het uitvoerbestand")
        print("4. Stoppen")

        keuze = input("Maak een keuze (1-4): ").strip()

        if keuze == "1":
            dagen = aantal_dagen(inputFile)
            print(f"Aantal dagen in invoerbestand: {dagen}")

        elif keuze == "2":
            auto_bereken(inputFile, outputFile)

        elif keuze == "3":
            result = overwrite_settings(outputFile)
            if result == 0:
                print("Waarde succesvol aangepast.")
            elif result == -1:
                print("Fout: datum niet gevonden.")
            elif result == -3:
                print("Fout: ongeldig systeem of waarde.")

        elif keuze == "4":
            print("Programma afgesloten.")
            break

        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    smart_app_controller()
