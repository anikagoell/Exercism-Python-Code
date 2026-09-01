def find(l, value):
    l.sort()
    start = 0
    end = len(l) - 1
    if value not in l:
        raise ValueError("value not in array")
    else:
        while start<=end:
            mid = (start + end)//2
            if l[mid] == value:
                return mid
            elif value > l[mid]:
                start = mid+1
            else:
                end = mid-1
            
            
        
