print("OPERADORES")
print("Operadores Aritméticos")
print("+ Suma de repuestos: ", 25, "+", 15,"=", 25+15)
print("- Descuento: ", 60, "-", 10,"=", 60-10)
print("* Precio por cantidad: ", 4, "*", 25,"=", 4*25)
print("/ Pago en cuotas: ", 300, "/", 3,"=", 300/3)
print("// Autos por bahia: ", 10, "//", 3,"=", 10//3)
print("% Autos sobrantes: ", 10, "%", 3,"=", 10%3)
print("** Potencia: ", 2, "**", 3,"=", 2**3)

print("Tabla de precios del cambio de aceite ($25)")
print(f"25 x 1 = {25*1}")
print(f"25 x 2 = {25*2}")
print(f"25 x 3 = {25*3}")
print(f"25 x 4 = {25*4}")
print(f"25 x 5 = {25*5}")
print(f"25 x 6 = {25*6}")
print(f"25 x 7 = {25*7}")
print(f"25 x 8 = {25*8}")
print(f"25 x 9 = {25*9}")
print(f"25 x 10 = {25*10}")

print("OPERADORES DE COMPARACION")
print("== Igual a :", 32, "==", 32, 32==32)
print("== Igual a :", 32, "==", 28, 32==28)

print("!= Distinto de :", 32, "!=", 28, 32!=28)
print("!= Distinto de :", 32, "!=", 32, 32!=32)

print("> Mayor que: ", 16000, ">", 8000, 16000>8000)
print("> Mayor que: ", 16000, ">", 20000, 16000>20000)

print("< Menor que: ", 16000, "<", 8000, 16000<8000)
print("< Menor que: ", 16000, "<", 20000, 16000<20000)

print(">= Mayor o igual que: ", 16000, ">=", 8000, 16000>=8000)
print(">= Mayor o igual que: ", 16000, ">=", 20000, 16000>=20000)

print("<= Menor o igual que: ", 16000, "<=", 8000, 16000<=8000)
print("<= Menor o igual que: ", 16000, "<=", 20000, 16000<=20000)

print("OPERADORES LOGICOS")
print("Operador and : (32==32)and(90>80)", (32==32)and(90>80))
print("Operador and : (32==32)and(90>100)", (32==32)and(90>100))
print("Operador or : (32==32)or(90>100)", (32==32)or(90>100))
print("Operador or : (32==28)or(90>100)", (32==28)or(90>100))
print("Operador not : not (32==28)", not (32==28))
print("Operador not : not (32==32)", not (32==32))

tiene_repuestos = True
taller_abierto = True

puede_reparar = tiene_repuestos and taller_abierto
print(f"Puede reparar? {puede_reparar}")

es_cliente_frecuente = True
tiene_dinero = False
acceso_credito = es_cliente_frecuente or tiene_dinero
print(f"Credito aprobado? {acceso_credito}")
