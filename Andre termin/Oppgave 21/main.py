class Person:
    def __init__(self, fornavn: str, etternavn:str) -> None:
        self.fornav = fornavn
        self.etternavn = etternavn

class BankKonto:
    def __init__(self, person: Person, kontonummer: int) -> None:
        self.person = person
        self.kontonummer = kontonummer
        self.saldo = 0
    def sett_inn_penger(self, inntekt) -> None:
        self.saldo += inntekt
    def ta_ut_penger(self, kostnadd) -> bool:
        if self.saldo >= kostnadd:
            self.saldo -= kostnadd
            return True
        return False
    
def main():
    Daniel = Person('Daniel', 'Gergerson')
    DanielBankKonto = BankKonto(Daniel, 1029312390)

    assert DanielBankKonto.ta_ut_penger(1) == False
    assert DanielBankKonto.saldo == 0
    DanielBankKonto.sett_inn_penger(10)
    assert DanielBankKonto.saldo == 10