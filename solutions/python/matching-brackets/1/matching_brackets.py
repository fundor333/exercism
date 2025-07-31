def is_paired(input_string):
    try:
        brachets = []
        for e in input_string:
            if e == "[":
                brachets.append("]")
            elif e == "(":
                brachets.append(")")
            elif e == "{":
                brachets.append("}")
            elif e == ")":
                if brachets.pop(-1) != ")":
                    return False
            elif e == "]":
                if brachets.pop(-1) != "]":
                    return False
            elif e == "}":
                if brachets.pop(-1) != "}":
                    return False
        return brachets == []
    except:
        return False
