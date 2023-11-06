from Uperson import UPerson      
class Lærer(UPerson):

    def __init__(self, fornavn: str, etternavn: str, fødsel: int, fag: list, kontaktlærerklasse: str) -> None:
        super().__init__(fornavn, etternavn, fødsel)
        self._fag = fag
        self._kontaktlærerklasse = kontaktlærerklasse
    def underviser_fag(self, bestemtfag) -> bool:
        if bestemtfag in self._fag:
            return True
        return False
    def __str__(self) -> None:
        return super().__str__() + f". Denne læreren er kontaktlærer hos {self._kontaktlærerklasse}"
    
