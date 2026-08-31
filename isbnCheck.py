def is_valid(isbn):
    sum=0
    j=10
    l = list()
    for i in isbn:
        if i.isdigit():
            l.append(int(i))
        elif i == 'X' or i == 'x': 
            l.append(10)
        elif i == '-':
            continue
        else:
            return False
    if len(l)!=10:
        return False
    if 10 in l[:-1]: 
        return False
    for i in l:
        c = int(i)*j
        sum+=c
        j-=1
    return sum % 11 == 0
