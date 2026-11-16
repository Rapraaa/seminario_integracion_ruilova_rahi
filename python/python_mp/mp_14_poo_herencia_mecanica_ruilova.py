class Vehiculo:
    modelo: str
    placa: str

    def __init__(self, modelo: str, placa: str):
        self.modelo = modelo
        self.placa = placa

    def mostrar_info(self):
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")

class Camioneta(Vehiculo):
    capacidad_carga: int

    def __init__(self, modelo: str, placa: str, capacidad_carga: int):
        super().__init__(modelo, placa)
        self.capacidad_carga = capacidad_carga

    def mostrar_carga(self):
        print(f"{self.modelo} carga hasta {self.capacidad_carga} kg")

class Moto(Vehiculo):
    def __init__(self, modelo: str, placa: str):
        super().__init__(modelo, placa)

    def revisar_cadena(self):
        print(f"Rahi Ruilova revisa la cadena de la {self.modelo}")

hilux = Camioneta("Toyota Hilux", "PBA-1234", 1000)
pulsar = Moto("Bajaj Pulsar", "AB-123C")

hilux.mostrar_info()
hilux.mostrar_carga()
pulsar.mostrar_info()
pulsar.revisar_cadena()
