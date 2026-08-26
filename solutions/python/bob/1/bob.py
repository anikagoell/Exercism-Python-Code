def response(hey):
    hey= hey.strip()
    if hey.endswith("?") and (not hey.isupper()):
        return "Sure."
    elif hey.isupper() and (not hey.endswith("?")):
        return "Whoa, chill out!" 
    elif hey.isspace() or not hey.strip():
        return "Fine. Be that way!" 
    elif hey.isupper() and hey.endswith("?"):
        return "Calm down, I know what I'm doing!" 
    else:
        return "Whatever."
