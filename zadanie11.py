lista = [0,1,2,3,4,5,6,7,8,9]
lista2 = []

print("   ", end="")
for m in range(10):
    print(f"{m:5}", end="")

for i in range(10):
    for j in range(10):
        val = (lista[i]) * (lista[j])
        lista2.append(val)
    print(lista2)
    lista2.clear()
