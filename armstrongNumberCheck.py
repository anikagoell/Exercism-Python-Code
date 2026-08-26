def is_armstrong_number(number):
    n = list(int(i) for i in str(number))
    tot = sum(i**len(n) for i in n)
    return tot==number
    
    
