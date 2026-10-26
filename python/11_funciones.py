print("Funciones: ")
print("Autor: Rahi Ruilova")

def kamehameha():
    print("Goku concentra su ki")
    print("Onda vitaaaaaaaaal")

kamehameha()

def atacar(guerrero):
    print(f"{guerrero} realiza un ataque de guerrero")

atacar("Gokusinho")
atacar("Raghisito")
atacar("El señor Ruilova")


def calcular_poder(poder, ataques):
    danio = poder * ataques
    return danio


print(f"El super mega poder de RAhi Ruilova es {calcular_poder(123123, 67 )}")


def transformar_sayayin(nombre:str, poder:int):
    if poder >= 9000:
        print(f"{nombre}, tu transformacion en super akusayang fue exitosa")
    else:
        print(f"{nombre} hay que comer la sopita, te falta poder")

transformar_sayayin('rahi', 99019203910293)
transformar_sayayin('jaimiti', 290)

nombre_personaje: str = "Rahi"
edad: int = 20
altura: float= 1.78
es_activo: bool = True

def multiplicador_poder(entrenamiento: float, edad: int)-> float:
    return entrenamiento*edad

print(multiplicador_poder(15, 23))
