import pickle

with open("logs.txt", "r") as f:
    data = f.read().split("/n")
    
    print(data)
