miasto_a = input("Podaj miasto 1")
miasto_b = input("Podaj miasto 2")
dystans = int(input("Podaj Dystans"))
cena_paliwa = float(input("cena paliwa: "))
spalanie = float(input("Spalanie na 100km : "))
out = round((dystans / 100) * spalanie * cena_paliwa, 2)

template = "Koszt przejazdu z {: 10} do  {:10} to: "


print(f"koszt przejazdu {miasto_a}-{miasto_b} to {cena_paliwa} PLN)")

input()








