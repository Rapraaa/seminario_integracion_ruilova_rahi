for tuerca in range (1, 5):
    print(f"Rahi Ruilova aprieta la tuerca numero: {tuerca}")

for llanta in range(1, 5):
    print(f"Revisando presion de la llanta {llanta}: 32 psi")


for vehiculo in range(1, 4):
    print(f"Vehiculo {vehiculo} \n")
    for llanta in range (1, 5):
      print(f"Vehiculo {vehiculo} - llanta {llanta} revisada")

vehiculos = [
    {"id": 1, "modelo": "Toyota Hilux", "placa": "PBA-1234", "estado": "En revision"},
    {"id": 2, "modelo": "Chevrolet Sail", "placa": "GYE-5678", "estado": "Reparado"},
    {"id": 3, "modelo": "Kia Sportage", "placa": "UIO-9012", "estado": "En espera"}
]

for vehiculo in vehiculos:
    print(vehiculo)

kilometrajes = {
    "Toyota Hilux" : 9500,
    "Chevrolet Sail" : 3200,
    "Kia Sportage" : 15000,
    "Ford F-150" : 4800,
}

for modelo, km in kilometrajes.items():
    if km >= 5000:
        print(f"{modelo} necesita cambio de aceite")
    else:
        print(f"{modelo} todavia esta bien")


print("Break y Continue")


for modelo in kilometrajes:
    if (modelo == "Kia Sportage"):
        break
    if (modelo == "Toyota Hilux"):
        continue
    print(f"Vehiculo: {modelo}")
