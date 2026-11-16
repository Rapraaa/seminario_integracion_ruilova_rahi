from abc import ABC, abstractmethod

class Servicio(ABC):
    @abstractmethod
    def realizar(self):
        pass

    @abstractmethod
    def costo(self) -> float:
        pass

class CambioAceite(Servicio):
    def realizar(self):
        return "Cambio de aceite realizado"

    def costo(self) -> float:
        return 35.50

class Alineacion(Servicio):
    def realizar(self):
        return "Alineacion y balanceo realizado"

    def costo(self) -> float:
        return 25.00

servicios = [CambioAceite(), Alineacion()]
total = 0
for servicio in servicios:
    print(f"{servicio.realizar()} - ${servicio.costo()}")
    total += servicio.costo()
print(f"Total a pagar a Rahi Ruilova: ${total}")
