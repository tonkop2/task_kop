def flatten_and_sort(array):
    for i, element in enumerate(array):

        if i == 0:
            summa0 = element
            summa0.sort()
            summa00 = summa0
        elif i == 1:
            summa1 = element
            summa1.extend(summa0)
            summa1.sort()
            summa00 = summa1
        elif i == 2:
            summa2 = element
            summa2.extend(summa1)
            summa2.sort()
            summa00 = summa2
        elif i == 3:
            summa3 = element
            summa3.extend(summa2)
            summa3.sort()
            summa00 = summa3
        elif i == 4:
            summa4 = element
            summa4.extend(summa3)
            summa4.sort()
            summa00 = summa4

    return summa00
