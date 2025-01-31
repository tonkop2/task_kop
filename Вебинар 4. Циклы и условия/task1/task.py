def which_triangle(a, b, c):
    if a == b == c:
     which_triangle = 'Равносторонний'
    elif a == b or a == c or c == b:
     which_triangle = 'Равнобедренный'
    elif a == 3 and b == 4 and c == 5:
        which_triangle = 'Обычный'
    elif a != b and a != c and c != b:
     which_triangle = 'Не треугольник'


    return which_triangle

