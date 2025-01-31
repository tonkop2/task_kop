def quadratic(b, c):
    import math
    a = 1

    discriminant = pow(b, 2) - 4*a*c
    check1 = (-b + math.sqrt(discriminant))/2 * a
    x1 = round(check1, 2)
    check2 = (-b - math.sqrt(discriminant))/2 * a
    x2 = round(check2, 2)
    return x1, x2

# x^2+bx+c=0
# a =1, b = -5, c = 4
# D = b^2 - 4ac
# x = -b - (корень)D / a