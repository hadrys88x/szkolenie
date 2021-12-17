def suma(*args):
    return sum(args)

def mul(*args):
    x = 1
    for i in args:
        x *= 1
    return x

def dzialania(*args, **kwargs):
    wynik = {}
    for dzialanie in kwargs:
        x = kwargs[dzialanie](*args)
        wynik[dzialanie] = x
    return wynik

print(dzialania(1,2,3, dodawanie=suma))