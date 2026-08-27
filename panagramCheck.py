def is_pangram(sentence):
    sentence = sentence.lower().strip()
    res = set()
    for i in list(sentence):
        if i.isalpha(): 
            res.add(i)
    return len(res) == 26
