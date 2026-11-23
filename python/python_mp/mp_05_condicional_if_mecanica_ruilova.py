print("Condicional if")
print("Condicional simple")
kilometraje = 8000
if kilometraje>=5000:
    print("Rahi Ruilova debe hacer el cambio de aceite")

print("Programa finalizo")

print("condicional if else")
print("condicional dos caminos")

dinero_cliente = float(input("Dinero disponible del cliente: \n"))
precio_repuesto = float(input("precio repuesto: "))

if (dinero_cliente>= precio_repuesto):
    print("Compra autorizada")
else:
    print("Dinero insuficiente")
    print("Buscar repuesto alternativo")

print("Condicional if - elif - else")
print("Condicional condicionales multiples")

aceite = float(input("Nivel de aceite del motor: "))

if (aceite >= 75):
    print("Aceite optimo")
elif (aceite >= 50):
    print("Aceite suficiente")
elif (aceite >= 25):
    print("Aceite bajo")
else:
    print("Critico")
    print("Cambiar aceite inmediatamente")

print("Condicional condiciones anidadas")
mecanico = input("Nombre del mecanico:")
frenos_funcionan = input("Los frenos funcionan? SI/NO: ")
aceite = int(input("Nivel de aceite disponible: "))

if (frenos_funcionan == "SI"):
    print("Frenos verificados")
    if aceite >= 50:
        print("Aceite suficiente")
        print("Vehiculo listo para entregar")
    else:
        print("Hay que cambiarle el aceite")
elif (frenos_funcionan == "NO"):
    print("No se puede entregar un auto sin frenos")
else:
    print("Debes escribir SI o NO")
