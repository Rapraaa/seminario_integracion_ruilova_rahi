print("Incluir datos con input")
nombre = input("cual es tu nombre?")

print("Hola", nombre, "bienvenido al taller")
print("Hola " + nombre + " bienvenido al taller")
print(f"Hola {nombre} bienvenido al taller")

cantidad = int(input("cuantos autos hay en el taller?"))
total = cantidad+2
print(f"Autos totales: {total}")

print("CONVERSIONES")
print("===Taller Mecanico Ruilova===")
nombre_cliente = input("Cual es tu nombre?")
precio = float(input("precio del repuesto?"))
cantidad = int(input("cantidad?"))
total = precio * cantidad
print(f"Total a pagar: {round(total, 2)}")
print(f"Total a pagar: ${total:.2f}")
