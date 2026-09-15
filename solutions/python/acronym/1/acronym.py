def abbreviate(w):
    w = w.replace('-',' ')
    newStr = ''
    for char in w:
        if char.isalpha() or char.isspace():
            newStr+= char
    res = []
    for i in newStr.split():
        if len(i)>0:
            res.append(i[0].upper())
    return ''.join(res)
        
    