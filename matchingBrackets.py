def is_paired(str):
    l = []
    d = {'}':'{', ')':'(', ']': '['}
    for i in str:
        if i in d.values():
            l.append(i)
        elif i in d.keys():
            if len(l)==0 or d[i] != l[-1]:
                return False
            l.pop()
    return len(l)==0
