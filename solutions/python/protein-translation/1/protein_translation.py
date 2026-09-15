def proteins(strand):
    i=0
    l = []
    while i < len(strand):
        code = strand[i:i+3]
        i = i+3
        if code.upper() in ['UAA','UAG','UGA']:
            return l
        elif code.upper() in ['AUG']:
            l.append("Methionine")
        elif code.upper() in ['UUU','UUC']:
            l.append("Phenylalanine")
        elif code.upper() in ['UUA','UUG']:
            l.append("Leucine")
        elif code.upper() in ['UCU','UCC','UCA','UCG']:
            l.append("Serine")
        elif code.upper() in ['UAU','UAC']:
            l.append("Tyrosine")
        elif code.upper() in ['UGU','UGC']:
            l.append("Cysteine")
        elif code.upper() in ['UGG']:
            l.append("Tryptophan")
        else:
            pass
    return l
