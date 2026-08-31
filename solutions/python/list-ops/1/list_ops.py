def append(list1, list2):
    list1.extend(list2)
    return list1


def concat(lists):
    l = []
    for i in lists:
        for n in i:
            l.append(n)

    return l


def filter(function, list):
    l = []
    for i in list:
        if function(i):
            l.append(i)
    return l


def length(list):
    return len(list)


def map(function, list):
    l = []
    for i in list:
        l.append(function(i))
        
    return l


def foldl(function, list, initial):
    l = initial
    if not list:
        return l
    else:
        for i in list:
                val = function(l, i)
                l = val
    return val


def foldr(function, list, initial):
    l = initial
    if not list:
        return l
    else:
        for i in reversed(list):
                val = function(l, i)
                l = val
    return val


def reverse(list):
    if list == []:
        return list
    else:
        return list[::-1]
