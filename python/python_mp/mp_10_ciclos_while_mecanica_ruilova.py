aceite = 0
while aceite < 4:
    print("Rahi Ruilova esta poniendo aceite al motor")
    aceite+= 1

print('El motor ya tiene 4 litros de aceite')

combustible = 40
while combustible > 0:
    print(f"Al tanque le quedan {combustible} litros")
    combustible -= 10
print("El tanque se quedo vacio, hay que ir a la gasolinera")


print("Continue y break")
dia = 0

while dia > -1:
    dia+=1
    if dia ==4:
        print("Dia 4: el taller esta cerrado")
        continue
    print(f"Dia {dia} Rahi Ruilova repara vehiculos")
    if dia == 6:
        print("Fin de la semana")
        break

pieza = 0
while pieza < 10:
    pieza += 1
    if pieza == 3:
        print("pieza en buen estado, se omite")
        continue
    if pieza == 7:
        print("Se encontro la falla, se detiene la revision")
        break
    print(f"Revisando la pieza {pieza}")
