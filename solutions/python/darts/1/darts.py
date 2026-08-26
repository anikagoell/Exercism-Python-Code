def score(x, y):
    sqDist = x**2 + y**2
    if sqDist <= 1:
        return 10
    elif 1 < sqDist <= 25:
        return 5
    elif 25< sqDist <= 100:
        return 1
    else:
        return 0
