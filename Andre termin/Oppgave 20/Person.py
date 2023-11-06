#Lager en klasse person som skal lagre informasjon som sier hvem personen er
class Person:
    def __init__(self, fornavn:str, etternavn:str, fødsel:int) -> None:
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødsel = fødsel