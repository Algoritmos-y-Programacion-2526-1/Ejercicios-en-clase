dictionary = {
    "pedro": {
        "edad": 20,
        "cedula": "V24545421",
        "universidad": "UNIMET"
    },
    "juan": {
        "edad": 22,
        "cedula": "V28454421",
        "universidad": "USB"
    },
}

for nombre, detalle in dictionary.items():
    print(nombre, detalle.get("universidad"))
    for caracteristica, valor in detalle.items():
        print(caracteristica, valor)