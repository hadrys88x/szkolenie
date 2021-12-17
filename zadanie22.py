def rekurencja(val: int):
    if val == 0: return 1

    n = val * (val - 1) ** 2
    print(n)
    rekurencja(n)

rekurencja(5)