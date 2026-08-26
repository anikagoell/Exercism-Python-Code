def classify(number):
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")
    tot = sum(factor(number))
    if tot==number:
        return "perfect"
    elif tot<number:
        return "deficient"
    else:
        return "abundant"
        
def factor(n):
    l=[]
    for i in range(1, n//2 +1):
        if n%i==0:
            l.append(i)
    return l
