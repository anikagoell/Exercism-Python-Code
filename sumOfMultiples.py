def sum_of_multiples(limit, multiples):
    low, high, *rest = multiples
    lowList = multiple(low, limit)
    highList = multiple(high, limit)
    s = set(lowList + highList) 
    return sum(s)

def multiple(n, limit):
    l = []
    for i in range(n, limit):
        if i % n == 0:
            l.append(i)
    return l
