
def function(text):
    start = False
    count = 0
    iterations = 0

    for j, v in enumerate(text):
        if (v == "<"):
            iterations += 1

    for i in range(iterations):
        for i, v in enumerate(text):
            if v == "<" and start == False:
                start = True
                continue
            elif v == ">":
                start = False
                continue
            elif start:
                if v != "<" and v != ">":
                    count += 1

        text.replace("<", "", 1)
    return count

print("Ilosc znakow: ", function("Ala ma <ko<ta>>"))