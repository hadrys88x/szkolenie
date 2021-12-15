x = int(input("podaj x"))
y = int(input("poday y"))

if (x > 100 or y > 100):
    print("Poza plansza")
elif (x <= 10) and (y >= 10):
    print("lewa krawedz")
elif(x <= 10) and (y >= 90):
    print("Gorny lewy róg")
elif (x <= 10) and (y < 90):
    print("lewy dolny rog")
elif (x >= 90 and y >= 90):
    print("Gorny prawy róg")
elif (x >= 90 and y >= 10):
    print("Prawa krawedz")
elif (x >= 90 and y < 10):
    print("Prawy dolny rog")
elif (x < 90 and y >= 90):
    print("Centrum gora")
elif (x < 90 and y >= 10):
    print("Centrum")
elif (x < 90 and y < 10):
    print("Centrum dol")
