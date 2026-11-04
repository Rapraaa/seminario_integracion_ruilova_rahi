print("Funciones: ")
print("Autor: Rahi Ruilova")

def abrir_taller():
    print("Se abre el Taller Ruilova")
    print("Bienvenidos")

abrir_taller()

def reparar(vehiculo):
    print(f"Rahi Ruilova repara el {vehiculo}")

reparar("Toyota Hilux")
reparar("Chevrolet Sail")
reparar("Kia Sportage")


def calcular_mano_obra(horas, precio_hora):
    total = horas * precio_hora
    return total


print(f"La mano de obra cuesta ${calcular_mano_obra(3, 15)}")


def revisar_aceite(modelo:str, kilometraje:int):
    if kilometraje >= 5000:
        print(f"{modelo} necesita cambio de aceite")
    else:
        print(f"{modelo} esta bien, puede seguir rodando")

revisar_aceite('Ford F-150', 8000)
revisar_aceite('Kia Sportage', 2000)

mecanico: str = "Rahi Ruilova"
anios_experiencia: int = 3
precio_aceite: float= 25.50
taller_abierto: bool = True

def calcular_total(precio_repuesto: float, cantidad: int)-> float:
    return precio_repuesto*cantidad

print(calcular_total(precio_aceite, 2))
