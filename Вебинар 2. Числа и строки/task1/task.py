




def square_calculation(a):
    import math

    perimeter = 4 * a
    calculation0 = pow(a, 2)
    square = round(calculation0, 2)  # возводим в степень 4
    calculation = math.sqrt(2) * a  # math - импортировали что бы можно было через него обращаться к корню sqrt
    diagonal = round(calculation, 2)  # простое округление, что округляем + до какого количества цифр
    return perimeter, square, diagonal
print(square_calculation(134.56))