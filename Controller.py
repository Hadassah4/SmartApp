import requests
import time

API_URL = "http://127.0.0.1:5000/api/weer"

def lees_weerdata():
    try:
        r = requests.get(API_URL)
        if r.status_code == 200:
            return r.json()
    except:
        print("Kan API niet bereiken.")
    return None

def bepaal_acties(weer):
    temp = weer.get("temperatuur", 0)
    vocht = weer.get("luchtvochtigheid", 0)
    wind = weer.get("windsnelheid", 0)
    gevoel = weer.get("gevoelstemperatuur", 0)

    if gevoel < 0:
        return "Verwarming op stand 5 (heel koud)"
    elif gevoel < 10:
        return "Verwarming op stand 3"
    elif gevoel > 25:
        return "Airco aan"
    else:
        return "Alles uit, temperatuur is prima"

def controller_loop():
    print("Controller gestart. Data wordt elke 10 seconden opgehaald.\n")
    while True:
        weer = lees_weerdata()
        if weer:
            actie = bepaal_acties(weer)
            print(f"Actie: {actie}")
        time.sleep(10)

if __name__ == "__main__":
    controller_loop()
