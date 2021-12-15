max = int(7)
temp = float(0)

while (max >= 1):
    temp += float(input("Podaj temperature "))
    max -= 1

print("Srednia temperatura: " + str(temp / 7))
