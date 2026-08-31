def flatten(iterable):
    finList= []
    for i in iterable:
        if isinstance(i, (list, tuple, set)):
            finList.extend(flatten(i))
        else:
            if i is not None :
                finList.append(i)
    return finList
    
    

    
