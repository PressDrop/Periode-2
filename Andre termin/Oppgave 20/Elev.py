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

def main():
    Daniel = Elev('Daniel', 'Gergerson', 2005)
    Viktor = Elev('Miriam', 'Vikingstad', 2006)
    Tien = Elev('Tien', 'Tran', 2007)

    Daniel.vis_info()
    Viktor.vis_info()
    Tien.vis_info()

if __name__ == '__main__':
    main()
    