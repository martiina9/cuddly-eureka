import json

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

vystup_json = open("prvni_json_soubor", mode="w", encoding="utf-8")
json.dump(chuckuv_slovnik, vystup_json, ensure_ascii=False)
vystup_json.close()