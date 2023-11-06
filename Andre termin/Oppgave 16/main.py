from Uperson import UPerson
class Elev(UPerson):

    def finn_trinn(self) -> bool: 
        #Vi antar at om det er mulig for eleven å gå på vgs, går eleven på vgs.
        if self.alder < 15:
            print("Denne eleven har ikke begynt på VGS enda")
            return False
        if self.alder > 19:
            print("Denne elven har sluttet på VGS")
            return False
        if self.alder == 15:
            print("Denne eleven går i vg1")
            return True
        if self.alder == 16:
            print("Denne elven går i enten vg1 eller vg2")
            return True
        if self.alder == 17:
            print("Denne elven går på enten vg1, vg2 eller vg3")
            return True
        if self.alder == 18:
            print("Denne elven går enten på vg2 eller vg3")
            return True
        if self.alder == 19:
            print("Denne elven går på vg3")
            return True
    def vis_info(self) -> None:
        super().vis_info()
        self.finn_trinn()
        
class Lærer(UPerson):
    def __init__(self, fornavn: str, etternavn: str, fødsel: int, fag: list, kontaktlærerklasse: str) -> None:
        super().__init__(fornavn, etternavn, fødsel)
        self.fag = fag
        self.kontaktlærerklasse = kontaktlærerklasse
    def underviser_fag(self, bestemtfag) -> bool:
        if bestemtfag in self.fag:
            return True
        return False
    def vis_info(self) -> None:
        super().vis_info()
        print(f"Denne læreren er kontaktlærer hos {self.kontaktlærerklasse}")
    

def main():
    Daniel = Elev('Daniel', 'Gergerson', 2005)
    Viktor = Elev('Miriam', 'Vikingstad', 2006)
    Tien = Elev('Tien', 'Tran', 2007)

    Miriam = Lærer('Miriam', 'Castillo Amo', 1989, ['Matte', 'IT2'], "1sta")
    Anders = Lærer('Anders', "Bark", 1988, ['Historie', 'Gym'], '3stn')


    Daniel.vis_info()
    Viktor.vis_info()
    Tien.vis_info()

    Miriam.vis_info()
    Anders.vis_info()
    assert Miriam.underviser_fag('IT2') == True
    assert Anders.underviser_fag('Gym') == True
    assert Anders.underviser_fag('IT2') == False

if __name__ == '__main__':
    main()
    