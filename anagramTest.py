def find_anagrams(word, candidates):
    ana = []
    word = word.lower()
    for i in candidates:
        if i.lower() == word:
            continue 
        else:
            if sorted(word) == sorted(i.lower()):
                ana.append(i)
    return ana
            
