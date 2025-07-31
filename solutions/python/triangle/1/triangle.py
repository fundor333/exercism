def check_inequality(sides):
    a,b,c = sides
    return all([a+b>=c, a+c>=b, b+c>=a,a>0,b>0,c>0])

def equilateral(sides):
    a,b,c = sides
    return (a==b and b==c and a==c) and check_inequality(sides)


def isosceles(sides):
    return (not scalene(sides)) and check_inequality(sides)


def scalene(sides):
    a,b,c = sides
    return (a!=b and b!=c and a!=c) and check_inequality(sides)
