import datetime

rok_urodzenia = int(input("Podaj rok urodzenia: "))
aktualny_rok = datetime.datetime.now().year

if (aktualny_rok - rok_urodzenia) < 18:
    print("Nie jestes Pelnoletni")
else:
    print("Jestes pelnoletni")