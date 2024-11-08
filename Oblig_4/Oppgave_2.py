import random

# Klasse for hvert enkelt kort
class Kort:
    def __init__(self, verdi, navn, farge):
        self.verdi = verdi       # Verdien til kortet (2-10, 10 for J/Q/K, 1/11 for Ess)
        self.navn = navn         # Navnet på kortet, f.eks. "To", "Konge", "Ess"
        self.farge = farge       # Fargen på kortet, f.eks. "hjerter", "spar", "kløver", "ruter"
    
    def __str__(self):
        # Returnerer kortets navn og farge som en streng for enkel utskrift
        return f"{self.farge} {self.navn}"

# Klasse for kortstokken
class Kortstokk:
    def __init__(self):
        # Oppretter en ny kortstokk med 52 kort
        self.kort = self.opprett_kortstokk()

    def opprett_kortstokk(self):
        # Oppretter en liste med kort som representerer en standard kortstokk
        kort = []
        verdier = list(range(2, 11)) + [10, 10, 10]  # Verdiene for kortene (2-10, og 10 for J/Q/K)
        navn = ['To', 'Tre', 'Fire', 'Fem', 'Seks', 'Sju', 'Åtte', 'Ni', 'Ti', 'Knekt', 'Dame', 'Konge', 'Ess']
        farger = ["Hjerter", "Kløver", "Spar", "Ruter"]  # Fargene for kortene

        # Legger til ett sett med hver verdi og fargekombinasjon
        for farge in farger:
            for i, verdi in enumerate(verdier):
                kort.append(Kort(verdi, navn[i], farge))  # Legger til kort med verdi, navn og farge
            kort.append(Kort(11, 'Ess', farge))  # Ess kan være 1 eller 11
        random.shuffle(kort)  # Blander kortene
        return kort

    def trekk_kort(self):
        # Trekker et kort fra bunken (fjernes fra kortstokken)
        return self.kort.pop() if self.kort else None

# Klasse for spiller og dealer
class Spiller:
    def __init__(self):
        # En liste som representerer kortene i spillerens hånd
        self.hand = []

    def legg_til_kort(self, kort):
        # Legger til et kort i spillerens hånd
        self.hand.append(kort)

    def beregn_sum(self):
        # Beregner totalverdien av kortene i hånden
        verdi = 0
        antall_ess = 0
        for kort in self.hand:
            verdi += kort.verdi
            if kort.navn == 'Ess':
                antall_ess += 1
        # Justerer ess-verdi fra 11 til 1 hvis totalverdien overstiger 21
        while verdi > 21 and antall_ess:
            verdi -= 10
            antall_ess -= 1
        return verdi

    def vis_hand(self, hide_first_card=False):
        # Viser kortene i hånden, med mulighet til å skjule første kort (for dealer)
        if hide_first_card:
            return f"{self.hand[1]} (Skjult kort)"
        return ', '.join([str(kort) for kort in self.hand])

# Klasse for hele Blackjack-spillet
class BlackjackSpill:
    def __init__(self, start_chips=100):
        # Setter antall chips spilleren starter med
        self.chips = start_chips
        # Oppretter en kortstokk
        self.kortstokk = Kortstokk()

    def start_runde(self):
        # Spør spilleren hvor mange chips de vil satse
        innsats = int(input(f'Du har {self.chips} chips. Hvor mye vil du satse?: '))
        if innsats <= 0 or innsats > self.chips:
            print('Ugyldig innsats')
            return

        # Oppretter ny kortstokk for hver runde
        self.kortstokk = Kortstokk()
        spiller = Spiller()
        dealer = Spiller()

        # Deler ut to kort til både spilleren og dealer
        for _ in range(2):
            spiller.legg_til_kort(self.kortstokk.trekk_kort())
            dealer.legg_til_kort(self.kortstokk.trekk_kort())

        # Sjekker om spilleren fikk blackjack
        if spiller.beregn_sum() == 21:
            self.chips += innsats * 1.5
            print(f'Blackjack! Du vinner 1,5x av innsatsen din! Du har nå {self.chips} chips')
            return

        # Spilleren velger "Hit" eller "Stand"
        while True:
            print(f'Dine kort: {spiller.vis_hand()} (Sum: {spiller.beregn_sum()})')
            print(f'Dealerens kort: {dealer.vis_hand(hide_first_card=True)}')
            valg = input('Vil du trekke eller stå? (trekke/stå): ')
            
            if valg.lower() == "trekke":  # Spilleren velger å trekke kort (Hit)
                spiller.legg_til_kort(self.kortstokk.trekk_kort())
                if spiller.beregn_sum() > 21:
                    # Spilleren har gått over 21 (Bust)
                    self.chips -= innsats
                    print(f'Dine kort: {spiller.vis_hand()} (Sum: {spiller.beregn_sum()})')
                    print(f'Du har tapt! Du har nå {self.chips} chips')
                    return
            elif valg.lower() == "stå":  # Spilleren velger å stå (Stand)
                break
            else:
                print('Ugyldig valg, vennligst velg "trekke" eller "stå".')

        # Dealerens tur til å trekke kort
        print("\nDealerens tur:")
        while dealer.beregn_sum() < 17:
            dealer.legg_til_kort(self.kortstokk.trekk_kort())

        dealer_sum = dealer.beregn_sum()
        print(f'Dealerens kort: {dealer.vis_hand()} Sum totalt: {dealer_sum}')

        spiller_sum = spiller.beregn_sum()

        # Sjekk hvem som vinner
        if dealer_sum > 21:
            # Dealer har bustet
            self.chips += innsats
            print(f'Dealeren bustet! Du vinner. Du har nå {self.chips} chips')
        elif dealer_sum > spiller_sum:
            # Dealer har høyere verdi enn spilleren
            self.chips -= innsats
            print(f'Du har tapt! Du har nå {self.chips} chips')
        elif dealer_sum < spiller_sum:
            # Spilleren har høyere verdi enn dealer
            self.chips += innsats
            print(f'Du vinner! Du har nå {self.chips} chips')
        else:
            # Det er uavgjort
            print(f'Uavgjort! Du har fortsatt {self.chips} chips')

    def spill(self):
        # Hovedspill-loop: fortsetter til spilleren er tom for chips eller velger å avslutte
        while True:
            self.start_runde()
            if self.chips <= 0:
                print('Du har gått tom for chips!')
                break
            fortsett = input('Vil du spille en runde til? (ja/nei): ')
            if fortsett.lower() != 'ja':
                print('Takk for at du spilte! Ha en fin dag!')
                break

# Starter spillet ved å lage et BlackjackSpill-objekt og kalle spill-metoden
spill = BlackjackSpill()
spill.spill()


