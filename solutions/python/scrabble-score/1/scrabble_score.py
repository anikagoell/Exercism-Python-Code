def score(word):
    sum = 0
    word = word.upper()
    for i in word:
        if i in 'AEIOULNRST':
            sum+=1
        elif i in 'DG':
            sum+=2
        elif i in 'BCMP':
            sum+=3
        elif i in 'FHVWY':
            sum+=4
        elif i in 'K':
            sum+=5
        elif i in 'JX':
            sum+=8
        else:
            sum+=10

    return sum
        
