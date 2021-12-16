produkty = {
    "marchew": 1.23,
    "cebula": 0.56,
    "ziemniaki": 2.21
}

print("W naszym sklepie oferujemy: ")
for produkt in produkty.items():
    print(produkt)

zakup = input("Co chcesz kupic?")

if zakup in produkty:
    ilosc = float(input("Podaj ilosc w kg: "))
    wartosc = produkty[zakup] * ilosc
    print("Cena: ", wartosc)
else:
    print("Nie posiadamy takiego produktu")