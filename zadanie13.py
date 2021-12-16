text = "Ala ma <kota>, a <kot> ma Alę"
count = 0
start = False

for i, v in enumerate(text):
    if v == "<":
        start = True
        continue
    elif v == ">":
        start = False
        continue
    elif start:
        count += 1

print("Ilosc znakow: ", count)