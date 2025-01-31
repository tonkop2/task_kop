lst = [1, 0, 1, 2, 0, 1, 3]
zero = []
neZero = []

for i in lst:
    if i == 0:
        zero += [i]
    else:
        neZero += [i]

lst = neZero + zero
print(lst)

def move_zeros(lst):
    zero = []
    neZero = []

    for i in lst:
        if i == 0:
            zero += [i]
        else:
            neZero += [i]

    lst = neZero + zero
    return lst
