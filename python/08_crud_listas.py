print("CRUD DE LISTAS EN PYTHON")
advengers = [
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": "Activo"},
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitan Amércia", "estado": "Activo"},
    {"id": 3, "nombre": "Thor Odinson", "heroe": "Thor", "estado": "Activo"}
]
id_publico = 4
def create():
    global id_publico
    print("Reclutar advenger")
    nombre = input("Nombre heroe: ")
    heroe = input("Heroe: ")
    estado = input("Estado (Activo, Retirado, Desaparecido)")
    nuevo_advenger = {
        "id": id_publico,
        "nombre": nombre,
        "heroe": heroe,
        "estado": estado
    }
    advengers.append(nuevo_advenger)
    id_publico += 1

def read():
    print("Lista de avengers")
    for avenger in advengers:
        print(f"{avenger["id"]} - nombre : {avenger["nombre"]}")

def update():
    print("Actualizar de avengers")
    id_update = int(input("Id a modificar: "))
    for avenger in advengers:
        if (avenger["id"] == id_update):
            avenger["nombre"] = input("Nuevo nombre: ")
            avenger["heroe"] = input("Nuevo heroe: ")
            avenger["estado"] = input("Nuevo estado: ")
            print("actualizado")

def delete():
    print("Borrar de avengers")
    id_update = int(input("Id a borrar: "))
    for avenger in advengers:
        if (avenger["id"] == id_update):
            advengers.remove(avenger)
            print("avenger elminado")

def menu():
    while True:
        print("Avengers")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")
        option=input("Seleccione 1 al 5: ")
        if option=="1":
            create()
        elif option=="2":
            read()
        elif option=="3":
            update()
        elif option=="4":
            delete()
        elif option=="5":
            print("Cerrando sistema")
            break
        else:
            print("Ingrese una opcion valida")

menu()
