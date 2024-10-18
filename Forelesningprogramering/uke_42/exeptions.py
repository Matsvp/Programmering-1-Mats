try:
    tall1 = int(input("Skriv inn et tall: "))
    tall2 = int(input("Skriv inn et annet tall: "))

    svaret = tall1 / tall2

    print(f"{tall1} delt på {tall2} er {svaret}")

except ValueError:
    print("Du må skrive inn et tall")


except NameError:
    print("Kunne ikke regne ut  noe svar")

except ZeroDivisionError:
    print("Kan ikke dele på 0")

else:
    print(svaret)
