"""
Instructions
Your task is to convert a number into its corresponding raindrop sounds.

If a given number:

is divisible by 3, add "Pling" to the result.
is divisible by 5, add "Plang" to the result.
is divisible by 7, add "Plong" to the result.
is not divisible by 3, 5, or 7, the result should be the number as a string.
"""
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
