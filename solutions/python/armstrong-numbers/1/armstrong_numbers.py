def is_armstrong_number(number):
    tot = 0
    num =len(str(number))
    for n in str(number):
        tot += pow(int(n),num)
    return number == tot
