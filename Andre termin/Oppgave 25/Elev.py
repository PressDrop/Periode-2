from Uperson import UPerson
class Elev(UPerson):

    def finn_trinn(self) -> str: 
        #Vi antar at om det er mulig for eleven å gå på vgs, går eleven på vgs.

        #Jeg har endret det fra å returnere en bool til å returnere en str slik at det kan bli lagt til på __str__
        if self._alder < 15:
            return "Denne eleven har ikke begynt på VGS enda"
        if self._alder > 19:
            return "Denne elven har sluttet på VGS"
        if self._alder == 15:
            return "Denne eleven går i vg1"
        if self._alder == 16:
            return "Denne elven går i enten vg1 eller vg2"
        if self._alder == 17:
            return "Denne elven går på enten vg1, vg2 eller vg3"
        if self._alder == 18:
            return "Denne elven går enten på vg2 eller vg3"
        if self._alder == 19:
            return "Denne elven går på vg3"
    def __str__(self) -> None:
        return super().__str__() + self.finn_trinn()

def main():
    Daniel = Elev('Daniel', 'Gergerson', 2005)
    Viktor = Elev('Miriam', 'Vikingstad', 2006)
    Tien = Elev('Tien', 'Tran', 2007)

    print(Daniel)
    print(Viktor)
    print(Tien)
if __name__ == '__main__':
    main()
    