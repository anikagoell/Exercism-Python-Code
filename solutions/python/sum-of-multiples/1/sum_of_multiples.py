def sum_of_multiples(limit, multiples):
    if not multiples:
        return 0    
    s = set()
    for m in multiples:
        if m == 0:
            continue
        s.update(getmultiples(m, limit))
    return sum(s)

def getmultiples(n, limit):
    l = []
    for i in range(n, limit):
        if i % n == 0:
            l.append(i)
    return l
