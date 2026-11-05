print("CRUD DE LISTAS EN PYTHON")
vehiculos = [
    {"id": 1, "modelo": "Toyota Hilux", "mecanico": "Rahi Ruilova", "estado": "En revision"},
    {"id": 2, "modelo": "Chevrolet Sail", "mecanico": "Carlos Perez", "estado": "Reparado"},
    {"id": 3, "modelo": "Kia Sportage", "mecanico": "Pedro Gomez", "estado": "En espera"}
]
id_publico = 4
def create():
    global id_publico
    print("Registrar vehiculo")
    modelo = input("Modelo del vehiculo: ")
    mecanico = input("Mecanico asignado: ")
    estado = input("Estado (En revision, Reparado, En espera): ")
    nuevo_vehiculo = {
        "id": id_publico,
        "modelo": modelo,
        "mecanico": mecanico,
        "estado": estado
    }
    vehiculos.append(nuevo_vehiculo)
    id_publico += 1

def read():
    print("Lista de vehiculos")
    for vehiculo in vehiculos:
        print(f"{vehiculo['id']} - modelo : {vehiculo['modelo']} - mecanico : {vehiculo['mecanico']} - estado : {vehiculo['estado']}")

def update():
    print("Actualizar vehiculo")
    id_update = int(input("Id a modificar: "))
    for vehiculo in vehiculos:
        if (vehiculo["id"] == id_update):
            vehiculo["modelo"] = input("Nuevo modelo: ")
            vehiculo["mecanico"] = input("Nuevo mecanico: ")
            vehiculo["estado"] = input("Nuevo estado: ")
            print("actualizado")

def delete():
    print("Eliminar vehiculo")
    id_delete = int(input("Id a eliminar: "))
    for vehiculo in vehiculos:
        if (vehiculo["id"] == id_delete):
            vehiculos.remove(vehiculo)
            print("vehiculo eliminado")
            break

def menu():
    while True:
        print("Taller Mecanico Ruilova")
        print("1. Registrar")
        print("2. Listar")
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
