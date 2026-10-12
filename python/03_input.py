print("Incluir datos con input")
nombre = input("cual es tu nombre?")

print("Hola", nombre, "bienvenido")
print("Hola " + nombre + " bienvenido")
print(f"Hola {nombre} bienvenido")

cantidad = int(input("cuantas rosquillas hay?"))
total = cantidad+2
print(f"Rosquillas totales: {total}")

print("CONVERSIONES")
print("===Tienda de apu===")
nombre_cliente = input("Cual es tu nombre ve?")
precio = float(input("precio?"))
cantidad = int(input("cantidad?"))
total = precio * cantidad
print(f"Total a pagar: {round(total, 2)}")
print(f"Total a pagar: ${total:.2f}")