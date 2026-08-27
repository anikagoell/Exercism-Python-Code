def to_rna(dna_strand):
    dna = list(dna_strand)
    rna= ''
    for i in dna:
        match (i):
            case 'G':
                rna+='C'
            case 'C':
                rna+='G'
            case 'T':
                rna+='A'
            case 'A':
                rna+='U'
            case _ :
                raise ValueError("Wrong DNA Strand entered")
    return rna
