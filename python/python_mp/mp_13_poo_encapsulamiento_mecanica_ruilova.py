class Vehiculo:
    placa: str
    __kilometraje: int

    def __init__(self, placa: str, kilometraje: int):
        self.placa = placa
        self.__kilometraje = kilometraje

    def get_kilometraje(self):
        return self.__kilometraje

    def registrar_viaje(self, km: int):
        if km > 0:
            self.__kilometraje += km
        else:
            print("Kilometraje no valido")

    def mostrar_info(self):
        print(f"Placa: {self.placa}")
        print(f"Kilometraje: {self.__kilometraje}")

hilux = Vehiculo("PBA-1234", 85000)
sail = Vehiculo("GYE-5678", 42000)

hilux.mostrar_info()
sail.mostrar_info()

hilux.registrar_viaje(150)
sail.registrar_viaje(-20)
print(f"Kilometraje actualizado por Rahi Ruilova: {hilux.get_kilometraje()}")
