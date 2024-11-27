from auto import Auto

class Berles:
    def __init__(self, auto: Auto, berlo_nev: str, napok_szama: int):
        self.auto = auto
        self.berlo_nev = berlo_nev
        self.napok_szama = napok_szama

    def teljes_koltseg(self):
        return self.napok_szama * self.auto.berleti_dij

    def __str__(self):
        return f"Bérlő: {self.berlo_nev}, Autó: {self.auto.rendszam}, Típus: {self.auto.tipus}, Napok száma: {self.napok_szama}, Teljes költség: {self.teljes_koltseg()} Ft"

