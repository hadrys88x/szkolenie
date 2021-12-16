def funkcja(text, min_count):
    result = set()
    for znak in set(text):
        if text.count(znak) > min_count:
            result.add(znak)
    return result

def test_wiecej_niz_dla_pustego_napisu():
    assert funkcja("", 4) == set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert funkcja("aaa", 1) == {"a"}
