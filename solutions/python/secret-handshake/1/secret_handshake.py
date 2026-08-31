def commands(binary_str):
    act = []
    for inx, num in enumerate(binary_str[::-1]):
        if num=="1":
            txt = action(inx)
            if txt == 'rev':
                act = act[::-1]
            else:
                act.append(txt)
    return act
        
def action(pos):
    if pos == 0: 
        return 'wink'
    elif pos == 1: 
        return 'double blink'
    elif pos == 2: 
        return 'close your eyes'
    elif pos == 3: 
        return 'jump'
    elif pos == 4: 
        return 'rev'
    else:
         pass
    