from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def info(self):
        pass

class Szemelyauto(Auto):
    def info(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap"

class Teherauto(Auto):
    def info(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap"

