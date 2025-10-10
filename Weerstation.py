print("Welkom bij het Weerstation!")
print("Voer per dag temperatuur (C), windsnelheid (m/s) en luchtvochtigheid (%) in.")
print("Druk op Enter bij de temperatuur om te stoppen.\n")

dagen_data = []
dag = 1

while dag <= 7:
    temp_input = input(f"Dag {dag} - temperatuur [°C]: ").strip()
    if temp_input == "":
        print("Programma gestopt (lege invoer).")
        break

    try:
        temp = float(temp_input)
    except ValueError:
        print("Ongeldige temperatuur, probeer opnieuw.")
        continue

    try:
        wind = float(input(f"Dag {dag} - windsnelheid [m/s]: "))
        vocht = float(input(f"Dag {dag} - luchtvochtigheid [%]: "))
    except ValueError:
        print("Ongeldige invoer, probeer opnieuw.")
        continue

    # Berekeningen
    temp_f = 32.0 + 1.8 * temp  # Fahrenheit berekenen
    gtemp = temp - (vocht / 100.0) * wind  # gevoelstemperatuur

    # Weerrapport
    if gtemp < 0:
        if wind > 10:
            rapport = "Het is heel koud en het stormt! Verwarming helemaal aan!"
        else:
            rapport = "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gtemp < 10:
        if wind > 12:
            rapport = "Het is best koud en het waait; verwarming aan en roosters dicht!"
        else:
            rapport = "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gtemp < 22:
        rapport = "Heerlijk weer, niet te koud of te warm."
    else:
        rapport = "Warm! Airco aan!"

    # Gemiddelde berekenen
    dagen_data.append(temp)
    gem_temp = sum(dagen_data) / len(dagen_data)

    # Resultaten 
    print(f"\nTemperatuur: {temp:.1f}°C ({temp_f:.1f}°F)")
    print(rapport)
    print(f"Gemiddelde temperatuur t/m dag {dag}: {gem_temp:.1f}°C")
    print("=" * 40 + "\n")

    dag += 1

print("Einde van het programma.")
