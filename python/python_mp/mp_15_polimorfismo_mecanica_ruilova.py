class Vehiculo:
    modelo: str

    def __init__(self, modelo: str):
        self.modelo = modelo

    def mantenimiento(self):
        print(f"{self.modelo}: revision general")

class Auto(Vehiculo):
    def mantenimiento(self):
        print(f"{self.modelo}: cambio de aceite y filtro")

class Camioneta(Vehiculo):
    def mantenimiento(self):
        print(f"{self.modelo}: revision de suspension y frenos")

class Moto(Vehiculo):
    def mantenimiento(self):
        print(f"{self.modelo}: ajuste de cadena y bujia")

vehiculos = [
    Auto("Chevrolet Sail"),
    Camioneta("Toyota Hilux"),
    Moto("Bajaj Pulsar"),
    Vehiculo("Vehiculo sin tipo"),
]

print("Mantenimientos del taller Ruilova")
for vehiculo in vehiculos:
    vehiculo.mantenimiento()
