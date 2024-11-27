from auto import Auto
from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev: str):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaadas(self, auto: Auto):
        self.autok.append(auto)

    def autok_listazasa(self):
        return [auto.info() for auto in self.autok]

    def berles_hozzaadas(self, berles: Berles):
        self.berlesek.append(berles)

    def berles_torlese(self, rendszam: str, berlo_nev: str):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.berlo_nev == berlo_nev:
                self.berlesek.remove(berles)
                return f"Bérlés törölve: {rendszam}, {berlo_nev}"
        return "Nem található bérlés."

    def berlesek_listazasa(self):
        if not self.berlesek:
            return ["Nincs aktív bérlés."]
        return [str(berles) for berles in self.berlesek]

