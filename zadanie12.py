lista = [2,4,5,6,8]
min = None
max = None
index = 0
index_max = 0
index_min = 0

for el in lista:
    if (min == None):
        min = el
        max = el
    if (el < min):
        min = el
        index_min = index
    if (el > max):
        max = el
        index_max = index
    index += 1

lista[index_min] = max
lista[index_max] = min

print(lista)