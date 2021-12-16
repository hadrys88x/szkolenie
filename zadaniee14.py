lista_samoglosek = ("a", "e", "i", "o", "u")
text = input("Podaj text: ")
count = 0

for i, v in enumerate(text):
    for j, vv in enumerate(lista_samoglosek):
        if v == vv:
            count += 1

print("Ilosc samoglosek: ", count)