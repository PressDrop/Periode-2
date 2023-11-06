from Uperson import UPerson      
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
    
