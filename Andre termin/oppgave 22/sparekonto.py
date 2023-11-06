from bankkonto import BankKonto, Person

class SpareKonto(BankKonto):
    def __init__(self, person: Person, kontonummer: int) -> None:
        super().__init__(person, kontonummer)
        self.maksuttak = 12
        self.nåværendeuttak = 0
    def ta_ut_penger(self, kostnadd) -> bool:
        if self.nåværendeuttak < self.maksuttak:
            if super().ta_ut_penger(kostnadd):
                self.nåværendeuttak += 1
                return True
        return False
    
def main():
    Daniel = Person('Daniel', 'Gergerson')
    DanielSpareKonto = SpareKonto(Daniel, 1029312390)

    DanielSpareKonto.sett_inn_penger(13)

    for i in range(15):
        DanielSpareKonto.ta_ut_penger(1)

    assert DanielSpareKonto.saldo == 1

if __name__ == '__main__':
    main()