from Elev import Elev
from Lærer import Lærer
class SkoleKlasse:
    def __init__(self, klassenavn:str, kontaktlærer: Lærer, klasseliste: list[Elev]) -> None:
        self.klassenavn = klassenavn
        self.kontaktlærer = kontaktlærer
        self.klasseliste = klasseliste
    def angi_kontaktlærer(self) -> None:
        print(f"Kontaktlæreren for {self.klassenavn} er {self.kontaktlærer.fornavn}")
    def legg_til_elev(self, elev:Elev) -> bool:
        if type(elev) == Elev:
            self.klasseliste.append(elev)
            return True
        return False
    def elever_i_klassen(self) -> False:
        print(f"Kontkatlæreren er {self.kontaktlærer.fornavn} og elevene er:")
        for i in range(len(self.klasseliste)):
            print(f"{i+1}. {self.klasseliste[i].fornavn} {self.klasseliste[i].etternavn}")

def main():
    Miriam = Lærer('Miriam', 'Castillo Amo', 1989, ["IT2", "Matte"], "3STN")

    Daniel = Elev('Daniel', 'Gergerson', 2005)
    Viktor = Elev('Miriam', 'Vikingstad', 2006)
    Tien = Elev('Tien', 'Tran', 2007)

    STN3 = SkoleKlasse('3STN', Miriam, [])
    STN3.legg_til_elev(Daniel)
    STN3.legg_til_elev(Viktor)
    STN3.legg_til_elev(Tien)

    STN3.elever_i_klassen()

if __name__ == '__main__':
    main()
    