def value(colors):
    a, b, *rest = colors
    sum = str(colorvalue(a)) + str(colorvalue(b))
    return int(sum)



def colorvalue(name):
    name = name.lower()
    d = {'black': 0, 'brown': 1,'red': 2,'orange': 3,'yellow': 4,'green': 5,'blue': 6,'violet':             7,'grey': 8,'white': 9 }
    return d[name]