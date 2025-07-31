def convert(number):
    out_str = ""
    if number % 3 == 0:
        out_str += "Pling"
    if number % 5 == 0:
        out_str += "Plang"
    if number % 7 == 0:
        out_str += "Plong"
    if len(out_str) == 0:
        return str(number)
    else:
        return out_str
