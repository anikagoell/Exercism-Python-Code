def slices(series, l):
    if not series:
        raise ValueError("series cannot be empty")
    elif l == 0:
        raise ValueError("slice length cannot be zero")
    elif l<0:
        raise ValueError("slice length cannot be negative")
    elif l > len(series):
        raise ValueError("slice length cannot be greater than series length")
    else:
        fin = []
        for i in range(len(series)-l+1):
            a = series[i:i+l]
            fin.append(a)
    return fin
