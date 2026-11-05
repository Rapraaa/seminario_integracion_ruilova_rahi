class Vehiculo:
    modelo: str
    placa: str
    kilometraje: int
    def __init__(self, modelo: str, placa: str, kilometraje: int):
        self.modelo = modelo
        self.placa = placa
        self.kilometraje = kilometraje

    def mostrar_info(self):
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Kilometraje: {self.kilometraje}")

hilux = Vehiculo("Toyota Hilux", "PBA-1234", 85000)
sail = Vehiculo("Chevrolet Sail", "GYE-5678", 42000)

hilux.mostrar_info()
sail.mostrar_info()
print(hilux.modelo)
print(sail.placa)


class Mecanico:
    nombre: str
    especialidad: str
    def __init__(self, nombre: str, especialidad: str):
        self.nombre = nombre
        self.especialidad = especialidad

    def reparar(self, vehiculo: Vehiculo):
        print(f"{self.nombre} repara el {vehiculo.modelo} ({self.especialidad})")

rahi = Mecanico("Rahi Ruilova", "Frenos y suspension")
rahi.reparar(hilux)
rahi.reparar(sail)
