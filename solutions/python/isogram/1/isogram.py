def is_isogram(phrase):
    letters = [char.lower() for char in phrase if char.isalpha()]
    return len(set(letters)) == len(letters)