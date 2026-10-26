poder = 2000
while poder < 10000:
    print("Vegetta esta entrenando")
    poder+= 2000

print('!Vegetta ya esta durisimo hermano!')

while poder > 0:
    print(f"Ese majimbu tiene {poder} de poder, esta muy duro")
    poder -= 500
print("Majinbu ya se quedo sin energia, a su casa calabaza")


print("Continue y break")
dia = 0

while dia > -1:
    dia+=1
    if dia ==4:
        print("Dia 4: gohan estudia")
        continue
    print(f"Dia {dia} Gohan entrena")
    if dia == 8:
        print("Fin del sistema")
        break

sectores = 0
while sectores < 10:
    sectores += 1
    if sectores == 3:
        print("zona destruida, se omitira este sector")
        continue
    if sectores == 7:
        print("Androides encontrados, se detendra la busqueda")
        break
    print(f"Trunks busca en el sector {sectores}")
