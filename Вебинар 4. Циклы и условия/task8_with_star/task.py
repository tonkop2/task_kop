num = 987
num4 = 1
num2 = str(num)
num5 = 1

for i, element in enumerate(num2):
    for b in range(9, 0, -1): #тут перебираем все числа от 0 до 9 что бы проверить ниже есть ли они в списке
        if b != int(element): #тут смотрим есть ли такая цифра в числе num
             num4 = num2[:i] + str(b) + num2[i+1:] #записываем сначала 1 цифру + цифра которой нет + все остальные цифры
        if int(num4) % 3 == 0: #тут остаток от деления если 0 значит это целое число.
            if(int(num5) < int(num4)):
                 num5 = int(num4)
            print(num4, "вход")
            print(num5, "выход")

def max_division_by_3(num):
    num4 = 1
    num2 = str(num)
    num5 = 1

    for i, element in enumerate(num2):
        for b in range(9, 0, -1): #тут перебираем все числа от 0 до 9 что бы проверить ниже есть ли они в списке
            if b != int(element): #тут смотрим есть ли такая цифра в числе num
                num4 = num2[:i] + str(b) + num2[i+1:] #записываем сначала 1 цифру + цифра которой нет + все остальные цифры
            if int(num4) % 3 == 0: #тут остаток от деления если 0 значит это целое число.
                if(int(num5) < int(num4)):
                    num5 = int(num4)
    return num5
