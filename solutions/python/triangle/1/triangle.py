def equilateral(sides):
    a,b,c = sides
    if valT(a,b,c):
        return a==b==c
    else:
        return False


def isosceles(sides):
    a,b,c = sides
    if valT(a,b,c):
        return a==b or b==c or c==a
    else:
        return False


def scalene(sides):
    a,b,c = sides
    if valT(a,b,c):
        return a!=b and b!=c and c!=a
    else:
        return False

def valT(a,b,c):
    if a>0 and b>0 and c>0:
        if a+b>=c and b+c>=a and a+c>=b:
            return True
            