

class MiejsceTeatralne:
    def __init__(self,numer,cena=0,dostepnosc=True):
        self.numer = numer
        self.cena = cena
        self.dostepnosc = dostepnosc

    def zarezerwuj(self):
        if not self.dostepnosc:
            print (f"Miejsce {self.numer} nie jest już dostępne")
            return False
        self.dostepnosc = False
        print(f"Miejsce {self.numer} zostało pomyślnie zarezerwowane")
        return True

    def anuluj_rezerwacje(self):
        if self.dostepnosc:
            print(f"Miejsce {self.numer} nie było zarezerwowane.")
            return False
        self.dostepnosc = True
        print(f"Rezerwacja miejsca {self.numer} została anulowana.")
        return True

    def __str__(self):
        status = "Wolne" if self.dostepnosc else "Niedostępne"
        return f"Miejsce {self.numer}, Cena: {self.cena} zł, Status: {status}"

class MiejsceParter(MiejsceTeatralne):
    def __init__(self, numer, cena=130, dostepnosc=True, wiecej_miejsca_na_nogi=True):
        super().__init__(numer, cena, dostepnosc)
        self.wiecej_miejsca_na_nogi= wiecej_miejsca_na_nogi
        self.typ = "Parter"

    def __str__(self):
        cechy = ", więcej miejca na nogi" if self.wiecej_miejsca_na_nogi else ""
        return f"{self.typ}, " + super().__str__() + cechy

# class MiejsceBalkon(MiejsceTeatralne):
#     def __init__(self, numer, cena=130, dostepnosc=True):
#         super().__init__(numer, cena, dostepnosc)
#
# class MiejsceLozaPrawa(MiejsceTeatralne):
#     def __init__(self,numer,cena=130,dostepnosc=True):
#         super().__init__(numer, cena, dostepnosc)
#
# class MiejsceLozaLewa(MiejsceTeatralne):
#     def __init__(self, numer, cena=130, dostepnosc=True):
#         super().__init__(numer,cena, dostepnosc)
#
# class MiejsceLozaSrodkowa(MiejsceTeatralne):
#     def __init__(self, numer, cena=260, dostepnosc=True, darmowy_szampan=True):
#         super().__init__(numer, cena, dostepnosc)
#         self.darmowy_szampan = darmowy_szampan
#
# class MiejscaOzN(MiejsceTeatralne):
#     def __init__(self,numer,cena=50,dostepnosc=True, blisko_wejscia=True):
#         super().__init__(numer,cena,dostepnosc)
#         self.blisko_wejscia = blisko_wejscia

M1 = MiejsceParter(2,34)
print(M1)
M1.zarezerwuj()
M1.anuluj_rezerwacje()
M1.zarezerwuj()

class Teatr:
    def __init__(self,nazwa):
        self.nazwa = nazwa
        self.miejsca = {}

    def dodaj_miejsce(self, miejsce: MiejsceTeatralne):
        if miejsce.numer in self.miejsca:
            print(f"Miejsce o numerze {miejsce.numer} już istnieje!")
            return
        self.miejsca[miejsce.numer] = miejsce

    def _utworz_miejsca(self):
        # PARTER – 14 rzędów po 35 miejsc, 130 zł
        for rzad in range(1, 15):          # 1–14
            for nr in range(1, 36):        # 1–35
                numer = f"P-{rzad}-{nr}"
                self.dodaj_miejsce(MiejsceParter(numer))

        # Miejsca dla OzN – 4 miejsca, 50 zł
        # for nr in range(1, 5):
        #     numer = f"OZN-{nr}"
        #     self.dodaj_miejsce(MiejscaOzN(numer))
        #
        # # BALKON I – 2 rzędy po 30 miejsc, 130 zł
        # for rzad in range(1, 3):           # 1–2
        #     for nr in range(1, 31):        # 1–30
        #         numer = f"B1-{rzad}-{nr}"
        #         self.dodaj_miejsce(MiejsceBalkonPierwszy(numer))
        #
        # # LOŻA PRAWA – 6 miejsc, 130 zł
        # for nr in range(1, 7):
        #     numer = f"LP-{nr}"
        #     self.dodaj_miejsce(MiejsceLozaPrawa(numer))
        #
        # # LOŻA LEWA – 6 miejsc, 130 zł
        # for nr in range(1, 7):
        #     numer = f"LL-{nr}"
        #     self.dodaj_miejsce(MiejsceLozaLewa(numer))
        #
        # # LOŻA ŚRODKOWA – 16 miejsc, 260 zł
        # for nr in range(1, 17):
        #     numer = f"LS-{nr}"
        #     self.dodaj_miejsce(MiejsceLozaSrodkowa(numer))
        #
        # # BALKON II – 4 rzędy po 40 miejsc, 110 zł
        # for rzad in range(1, 5):           # 1–4
        #     for nr in range(1, 41):        # 1–40
        #         numer = f"B2-{rzad}-{nr}"
        #         self.dodaj_miejsce(MiejsceBalkonDrugi(numer))
        #
        # # BALKON III – 6 rzędów po 30 miejsc, 90 zł
        # for rzad in range(1, 7):           # 1–6
        #     for nr in range(1, 31):        # 1–30
        #         numer = f"B3-{rzad}-{nr}"
        #         self.dodaj_miejsce(MiejsceBalkonTrzeci(numer))

    def pokaz_miejsca(self):
        for miejsce in self.miejsca.values():
            print(miejsce)

    def pokaz_wolne_miejsca(self):
        for miejsce in self.miejsca.values():
            if miejsce.dostepnosc:
                print(miejsce)

    def zarezerwuj_miejsce(self,numer):
        miejsce = self.miejsca[numer]
        if not miejsce:
            print(f"Miejsce {numer} nie istnieje.")
            return False
        return miejsce.zarezerwuj()

T1 = Teatr("Teatr Wielki")
T1._utworz_miejsca()
T1.pokaz_wolne_miejsca()