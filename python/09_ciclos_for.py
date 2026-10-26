for flexion in range (1, 5):
    print(f"Jaime antonio hace la flexion numero: {flexion}")

for tabla in range(1, 11):
    print(f"Multiplicacion {tabla} x 2 = {tabla * 2}")


for tabla in range(1, 11):
    print(f"Tabla del {tabla} \n")
    for numero in range (1, 11):
      print(f"Multiplicacion {tabla} x {numero} = {tabla * numero}")

advengers = [
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": "Activo"},
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitan Amércia", "estado": "Activo"},
    {"id": 3, "nombre": "Thor Odinson", "heroe": "Thor", "estado": "Activo"}
]

for avenger in advengers:
    print(avenger)

guerreros = {
    "Goku" : 9500,
    "Vergetta" : 19500,
    "Gojan" : 30,
    "Broli" : 2300,
}

for nombre, poder in guerreros.items():
    if poder >= 9000:
        print(f"{nombre} puede enfrentar a freezer")
    else:
        print(f"{nombre} necesita entrenar mas")


print("Break y Continue")


for guerrero in guerreros:
    if (guerrero == "Gojan"):
        break
    if (guerrero == "Goku"):
        continue
    print(f"Guerrero: {guerrero}")
