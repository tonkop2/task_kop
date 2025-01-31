def modification(lst):
    x = lst[0]
    y = lst[-1]
    lst[0] = y
    lst[-1] = x
    return lst
