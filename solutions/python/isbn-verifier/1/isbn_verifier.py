import re


def verify(isbn):
    if len(re.sub("[^0-9Xx]+", "", isbn)) != 10:
        return False
    t = re.sub("[^0-9]+", "", isbn)
    total = 0
    i = 10
    if len(t) != 10:
        total += 10
    for e in t:
        total += int(e) * i
        i -= 1
    return total % 11 == 0