def convert(n):
    text=""
    if n%3==0:
        text+="Pling"
    if n%5==0:
        text+="Plang"
    if n%7==0:
        text+="Plong"
    if text=="":
        return str(n)
    else:
        return text
        
