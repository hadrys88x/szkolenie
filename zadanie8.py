min = ""
max = ""

while (True):
    value = input("Podaj wartosc")

    if (value == "end"):
        break
    elif (value.isnumeric()):
        print("Niepoprawna wartosc")
        continue
    value = int(value)

    if (min == ""):
        min = value
        max = value
    elif (min < value):
        min = value
    elif (max > value):
        max = value

    print("Wartosc minimalna: " + str(min) + ", Wartosc maksymalna: " + str(max))
