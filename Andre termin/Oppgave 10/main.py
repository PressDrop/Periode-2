from Person import Person
#Egentlig burde jeg kanskje ikke bruke arv her gitt at det bare er en utviddelse av klassen Person
class UPerson(Person):
    def __init__(self, fornavn:str, etternavn:str, fødsel:int) -> None:
        super().__init__(fornavn, etternavn, fødsel)
        self.alder = self.beregn_alder()
    def beregn_alder(self) -> int: #Beregner alder via at året er 2023 og du har bursdagen deres
        return 2023 - self.fødsel
    #Bruker alderen beregnet via beregn_alder
    def vis_info(self) -> None:
        print(f"{self.fornavn} {self.etternavn} er {self.alder} år gammel")

def main():
    Daniel = UPerson('Daniel', 'Gergerson', 2005)
    Miriam = UPerson('Miriam', 'Castillo Amo', 1999)
    Tien = UPerson('Tien', 'Tran', 1990)

    Daniel.vis_info()
    Miriam.vis_info()
    Tien.vis_info()

if __name__ == '__main__':
    main()