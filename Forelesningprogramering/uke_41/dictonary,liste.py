brettspill = [
    {'tittel':'Dixit', 'spilletid':30, 'aldersgrense':8, 'år':2008},
    {'tittel':'Pandemic', 'spilletid':45, 'aldersgrense':8, 'år':2000},
    {'tittel':'Wingspan', 'spilletid':40, 'aldersgrense':10, 'år':2019}
]

print(brettspill)

for spill in brettspill:
    print(f'{spill['tittel']} er ment for spillere fra {spill['aldersgrense']} år og oppover')

brettspill.append({'tittel': 'Mysterium', 'spilletid':42, 'aldersgrense':10, 'år':2005})
print(brettspill)

print(brettspill[0])