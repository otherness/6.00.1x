def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    
    inv_d = {}
    for item in d.itervalues():
        if not item in inv_d:
            inv_d[item] = []

    for key in inv_d:
        lst = []
        for k in d:
            if d[k] == key:
                lst.append(k)
        inv_d[key] = sorted(lst)
        
    return inv_d
    

#d = {1:10, 2:20, 3:30, 4:30}
#d = {4:True, 2:True, 0:True}

print dict_invert(d)
            
        