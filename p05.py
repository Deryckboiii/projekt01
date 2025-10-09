class Teglalap():
    alakzat = "téglalap"
    def __init__(self, alap = 10, magassag = 5):
        self.alap = alap
        self.magassag = magassag

    def adatok(self):
        print(f"A {self.alakzat} alapja = {self.alap}")
        print(f"A {self.alakzat} magassága = {self.magassag}")

    def kerulet(self):
        return 2 * self.alap + 2 * self.magassag

    def terulet(self):
        return self.alap * self.magassag

class Negyzet(Teglalap):
    alakzat = "negyzet"
    def __init__(self, alap = 5):
        super().__init__()
        self.alap = alap
        self.magassag = alap

    def adatok(self):
        print(f"A {self.alakzat} alapja = {self.alap}")

class Haromszog(Teglalap):
    alakzat = "háromszög"
    def __init__(self, alap = 10, magassag = 5):
        super().__init__()
        self.alap = alap
        self.magassag = magassag

    def terulet(self):
        return (self.alap * self.magassag) / 2


tegla = Teglalap(20,15)
print(tegla.adatok())
print("A kerülete = ", tegla.kerulet())
print("A területe = ", tegla.terulet())
print()

negy = Negyzet(8)
print(negy.adatok())
print("A kerülete = ", negy.kerulet())
print("A területe = ", negy.terulet())
print()

harom = Haromszog()
print(harom.adatok())
print("A területe = ", harom.terulet())
print()

