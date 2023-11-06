from Person import Person
#Egentlig burde jeg kanskje ikke bruke arv her gitt at det bare er en utviddelse av klassen Person
#Klate den kun Uperson for å lage et skille mellom den oppdaterte klassen og den orginale klassen
class UPerson(Person):
    def __init__(self, fornavn:str, etternavn:str, fødsel:int) -> None:
        super().__init__(fornavn, etternavn, fødsel)
        self._alder = self.beregn_alder()
    def beregn_alder(self) -> int: #Beregner alder via at året er 2023 og du har bursdagen deres
        return 2023 - self._fødsel
    #Bruker alderen beregnet via beregn_alder
    def __str__(self) -> None:
        return f"{self._fornavn} {self._etternavn} er {self._alder} år gammel"

def main():
    Daniel = UPerson('Daniel', 'Gergerson', 2005)
    Miriam = UPerson('Miriam', 'Castillo Amo', 1999)
    Tien = UPerson('Tien', 'Tran', 1990)

    print(Daniel)
    print(Miriam)
    print(Tien)

if __name__ == '__main__':
    main()