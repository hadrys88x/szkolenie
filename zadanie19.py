def funkcja(text, min_count):
    result = set()
    for znak in set(text):
        if text.count(znak) > min_count:
            result.add(znak)
        return result

assert funkcja("", 4) == set()
assert funkcja("aaa", 1) == "a"
