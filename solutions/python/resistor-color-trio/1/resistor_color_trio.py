def label(colors):
    a, b, c, *d = colors
    c = colorvalue(c)
    str = ''
    for i in range (c):
        str+='0'
    sum = int(value([a,b])+str)
    if sum<1000:
        return (f"{sum} ohms")
    elif sum<1000000:
        sum = sum//1000
        return (f"{sum} kiloohms")
    elif sum<1000000000:
        sum = sum//1000000
        return (f"{sum} megaohms")
    else:
        return (f"{sum//1000000000} gigaohms")


def value(colors):
    a, b, *rest = colors
    sum = str(colorvalue(a)) + str(colorvalue(b))
    return sum


def colorvalue(name):
    name = name.lower()
    d = {'black': 0, 'brown': 1,'red': 2,'orange': 3,'yellow': 4,'green': 5,'blue': 6,'violet':             7,'grey': 8,'white': 9 }
    
    return d[name]