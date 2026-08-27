def rotate(text, key):
    res = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + key) % 26)
            res.append(new_char)
        else:
            res.append(char)
    return "".join(res)
