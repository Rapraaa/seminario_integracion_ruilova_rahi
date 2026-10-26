"""
Manejoo de cadenas de caracteres
"""

nombre1="Rahi Ruilova"
print(f"Jedi 1: {nombre1}")
print(f"Tipo de datos: {type(nombre1)}")

nombre2="Pepe Etesech"
print(f"Jedi 2: {nombre2}")
print(f"Tipo de datos: {type(nombre2)}")

####### Funciones comunes de las variables string
print("Funciones comunes de texto")
droide1 = "caca"
droide2 = "droidecaca2"
longitud_droide1 = len(droide1)
longitud_droide2 = len(droide2)
print("nombre droide 1:", droide1)
print("longitud droide 1:", longitud_droide1)
print("nombre droide 2:", droide2)
print("longitud droide 2:", longitud_droide2)

print("Convertir mayusculas en minusculas")
mensaje = "El rahi le gusta el maracuya"
mensaje_mayuscula = mensaje.upper()
mensaje_minuscula= mensaje.lower()
print("Mensaje original", mensaje)
print("Mensaje mayusculas", mensaje_mayuscula)
print("Mensaje ominusculas", mensaje_minuscula)

print("Reemplazo de substring")
mensaje = "El rahi le gusta el maracuya y el mango"
nuevo_mensaje = mensaje.replace("maracuya", "manzana")
print("Mensaje original", mensaje)
print("Mensaje modificado", nuevo_mensaje)

planetas = "tierra, marte, jupiturno"
print("planetas", planetas)
lista_planetas = planetas.split(',')
print(lista_planetas)
print("Primer planeta : ", lista_planetas[0])

print("Extraer subcadenas")
mensaje = "Que la fuerza te acompañe siempre"
adjetivo = mensaje[7:13]
verbo = mensaje[17:26]
print("adjetivo es: ", adjetivo)
print("verbo es: ", verbo)

print("Comprobaciones utiles")
codigo = "R2D2"
numero = "2026"
nombre = 'UniversidadUTE'
identificador = "pepe2"
print(codigo.isalnum())
print(numero.isdigit())
print(nombre.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())
