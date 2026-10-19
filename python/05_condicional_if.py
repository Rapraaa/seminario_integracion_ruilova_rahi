print("Condicional if")
print("Condicional simple")
dinero = 10
if dinero>=5:
    print("Rahi si puede comprar rosquillas")

print("Programa finalizo")

print("condicional if else")
print("condicional dos caminos")

creditos = float(input("Cantidad de cretidos disponibles: \n"))
precio_repuesto = float(input("precio repuesto: "))

if (creditos>= precio_repuesto):
    print("Compra autorizada")
else: 
    print("Creditos insuficientes")
    print("Buscar solucion o trueque")

print("Condicional if - elif - else")
print("Condicional condicionales multiples")

combustible = float(input("Combustible de la nave: "))

if (combustible >= 75):
    print("Combustible optimo")
if (combustible >= 50):
    print("Combustible suficiente")
if (combustible >= 25):
    print("Combustible bajo")
else:
    print("Critico")
    print("Localiza base mas cercana")

print("Condicional condiciones anidadas")
piloto = input("Nombre del piloto:")
motor_funciona = input("El motor funciona? SI/NO: ")
combustible = int(input("Combustible disponible: "))

if (motor_funciona == "SI"):
    print("Motor verificado")
    if combustible >= 50:
        print("Combustivle suficiente")
        print("Participacion autorizada")
    else:
        print("Metale gasolina mijo")
elif (motor_funciona == "No"):
    print("como vas a arrancar sin motor mijito")
else:
    print("dice SI o NO, debes escribir eso no otra cosa e")