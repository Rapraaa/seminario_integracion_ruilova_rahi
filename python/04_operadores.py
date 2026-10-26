print("OPERADORES")
print("Operadores Aritméticos")
print("+ Suma: ", 5, "+", 3,"=", 5+3)
print("- Resta: ", 5, "-", 3,"=", 5-3)
print("* Multiplicación: ", 5, "*", 3,"=", 5*3)
print("/ División: ", 15, "/", 3,"=", 15/3)
print("// División entera: ", 10, "//", 3,"=", 10//3)
print("% Residuo: ", 10, "%", 3,"=", 10%3)
print("** Potencia: ", 2, "**", 3,"=", 2**3)

print("Tabla del 5")
print(f"5 x 1 = {5*1}")
print(f"5 x 2 = {5*2}")
print(f"5 x 3 = {5*3}")
print(f"5 x 4 = {5*4}")
print(f"5 x 5 = {5*5}")
print(f"5 x 6 = {5*6}")
print(f"5 x 7 = {5*7}")
print(f"5 x 8 = {5*8}")
print(f"5 x 9 = {5*9}")
print(f"5 x 10 = {5*10}")

#Operadores Aritmeticos

print("Operadores")

print("Operadores Aritmeticos")

print("+ Suma: ", 5, "+", 3, "=", 5+3)
print("- Resta: ", 5, "-", 3, "=", 5-3)
print("* Multiplicacion: ", 5, "*", 3, "=", 5*3)
print("/ Division: ", 15, "/", 3, "=", 15/3)
print("// Division entera: ", 10, "//", 3, "=", 10//3)
print("% Residuo: ", 10, "%", 3, "=", 10%3)
print("** Potencia: ", 10, "**", 3, "=", 2**3)


print("OPERADORES DE COMPARACION")
print("== Igual a :", 5, "==", 5, 5==5)
print("== Igual a :", 5, "==", 4, 5==4)

print("!= Igual a :", 5, "==", 4, 5!=5)
print("!= Igual a :", 5, "==", 5, 5!=5)

print("> Mayor que: ", 10, ">", 8, 10>8)
print("> Mayor que: ", 10, ">", 18, 10>18)

print("< Menor que: ", 10, "<", 8, 10<8)
print("< Menor que: ", 10, "<", 18, 10<18)

print("> Mayor o igual que: ", 10, ">=", 8, 10>=8)
print("> Mayor o igual que: ", 10, ">=", 18, 10>=18)

print("< Menor o igual que: ", 10, "<=", 8, 10<=8)
print("< Menor o igual que: ", 10, "<=", 18, 10<=18)

print("OPERADORES LOGICOS")
print("Operador and : (5==5)and(4>3)", (5==5)and(4>3))
print("Operador and : (5==5)and(4>8)", (5==5)and(4>8))
print("Operador or : (5==5)or(4>8)", (5==5)or(4>8))
print("Operador or : (5==6)or(4>8)", (5==6)or(4>8))
print("Operador not : not (5==6)", not (5==6))
print("Operador not : not (5==5)", not (5==5))

tiene_dinero = True
tienda_abierta = True

puede_comprar = tiene_dinero and tienda_abierta
print(f"Puede comprar? {puede_comprar}")

es_vip = True
tiene_dinero = False
acceso_credito = es_vip or tiene_dinero
print(f"Credito aprobado? {acceso_credito}")