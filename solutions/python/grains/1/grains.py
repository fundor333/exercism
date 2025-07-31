def square(number):
    if not(1<=number<=64):
        raise ValueError("square must be between 1 and 64") 
    t = 1
    for i in range(number-1):
        t *= 2
    return t

def total():
    return 18446744073709551615
