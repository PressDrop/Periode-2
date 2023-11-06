from bankkonto import BankKonto, Person

#Jeg tolker oppgaven som at man kun kan ta ut penger en gang før hele kontoen blir deaktivert
class BSU(BankKonto):
    def __init__(self, person: Person, kontonummer: int) -> None:
        super().__init__(person, kontonummer)
        self.brukbar_konto = True
    def sett_inn_penger(self, inntekt) -> None:
        if self.brukbar_konto:
            return super().sett_inn_penger(inntekt)
    def ta_ut_penger(self) -> True:
        if self.brukbar_konto:
            print("Du har tatt ut alle pengene fra kontoen, kontoen blir nå dekativert")
            self.saldo = 0
            self.brukbar_konto = False
            return True
    
def main():
    Daniel = Person('Daniel', 'Gergerson')
    DanielBSU = BSU(Daniel, 1029312390)

    DanielBSU.sett_inn_penger(13)

    DanielBSU.ta_ut_penger()

    assert DanielBSU.saldo == 0
    DanielBSU.sett_inn_penger(12)
    assert DanielBSU.saldo == 0

if __name__ == '__main__':
    main()