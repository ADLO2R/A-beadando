from auto import Szemelyauto, Teherauto
from berles import Berles
from autokolcsonzo import Autokolcsonzo

def main():
    kolcsonzo = Autokolcsonzo("Autókölcsönző")

   
    auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 10000)
    auto2 = Szemelyauto("DEF-456", "Ford Focus", 12000)
    auto3 = Teherauto("GHI-789", "Mercedes Sprinter", 15000)
    
    kolcsonzo.auto_hozzaadas(auto1)
    kolcsonzo.auto_hozzaadas(auto2)
    kolcsonzo.auto_hozzaadas(auto3)

    
    kolcsonzo.berles_hozzaadas(Berles(auto1, "Kovács Béla", 3))
    kolcsonzo.berles_hozzaadas(Berles(auto2, "Nagy Anna", 2))

    while True:
        print("\n1. Autók listázása\n2. Autó bérlése\n3. Bérlés lemondása\n4. Bérlések listázása\n5. Kilépés")
        valasz = input("Választás: ")

        if valasz == "1":
            for auto in kolcsonzo.autok_listazasa():
                print(auto)
        elif valasz == "2":
            rendszam = input("Rendszám: ")
            berlo_nev = input("Bérlő neve: ")
            napok_szama = int(input("Napok száma: "))
            auto = next((a for a in kolcsonzo.autok if a.rendszam == rendszam), None)
            if auto:
                berles = Berles(auto, berlo_nev, napok_szama)
                kolcsonzo.berles_hozzaadas(berles)
                print(f"Bérlés hozzáadva: {berles}")
            else:
                print("Nem található autó ezzel a rendszámmal.")
        elif valasz == "3":
            rendszam = input("Rendszám: ")
            berlo_nev = input("Bérlő neve: ")
            print(kolcsonzo.berles_torlese(rendszam, berlo_nev))
        elif valasz == "4":
            for berles in kolcsonzo.berlesek_listazasa():
                print(berles)
        elif valasz == "5":
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()

