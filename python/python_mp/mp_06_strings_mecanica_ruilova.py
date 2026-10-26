mecanico1="Rahi Ruilova"
print(f"Mecanico 1: {mecanico1}")
print(f"Tipo de datos: {type(mecanico1)}")

mecanico2="Carlos Perez"
print(f"Mecanico 2: {mecanico2}")
print(f"Tipo de datos: {type(mecanico2)}")

print("Funciones comunes de texto")
auto1 = "Hilux"
auto2 = "Sportage"
longitud_auto1 = len(auto1)
longitud_auto2 = len(auto2)
print("nombre auto 1:", auto1)
print("longitud auto 1:", longitud_auto1)
print("nombre auto 2:", auto2)
print("longitud auto 2:", longitud_auto2)

print("Convertir mayusculas en minusculas")
mensaje = "Rahi Ruilova repara el motor de la camioneta"
mensaje_mayuscula = mensaje.upper()
mensaje_minuscula= mensaje.lower()
print("Mensaje original", mensaje)
print("Mensaje mayusculas", mensaje_mayuscula)
print("Mensaje minusculas", mensaje_minuscula)

print("Reemplazo de substring")
mensaje = "Rahi Ruilova cambia el aceite y los frenos"
nuevo_mensaje = mensaje.replace("aceite", "filtro")
print("Mensaje original", mensaje)
print("Mensaje modificado", nuevo_mensaje)

repuestos = "bujias,filtro,pastillas"
print("repuestos", repuestos)
lista_repuestos = repuestos.split(',')
print(lista_repuestos)
print("Primer repuesto : ", lista_repuestos[0])

print("Extraer subcadenas")
mensaje = "El motor esta listo para entregar"
sustantivo = mensaje[3:8]
verbo = mensaje[25:33]
print("sustantivo es: ", sustantivo)
print("verbo es: ", verbo)

print("Comprobaciones utiles")
placa = "PBA1234"
anio = "2020"
marca = 'Toyota'
codigo_repuesto = "rep24"
print(placa.isalnum())
print(anio.isdigit())
print(marca.isalpha())
print(codigo_repuesto.isalnum())
print(codigo_repuesto.isdigit())
