lista = [22,1,4,5,9,3,7,8]
print(lista)

for j in range(len(lista)):
    for i, v in enumerate(lista):
        if i != 0 and v < lista[i - 1]:
            replace_1 = v
            replace_2 = lista[i - 1]
            lista[i] = replace_2
            lista[i-1] = replace_1

print(lista)