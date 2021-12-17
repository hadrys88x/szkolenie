import pickle

list = ["xxx", "yyy", "zzz"]

with open("plik.txt", "wb") as f:
    f.write(pickle.dumps(list))

with open("plik.txt", "rb") as f:
    data = pickle.load(f)
    for i, v in enumerate(data):
        print(f"{i+1}: {v}")
