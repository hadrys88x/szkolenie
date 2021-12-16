lista = []

for i in range(10):
    operacja = input("Podaj liczbe lub k by zakonczyc: ")
    if (operacja == "k"):
        break
    liczba = int(operacja)
    lista.append(liczba)

print(sum(lista) / len(lista))