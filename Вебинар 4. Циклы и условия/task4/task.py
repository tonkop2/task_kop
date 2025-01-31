def multiplication_chain(num):
    work = 1
    number_of_iterations = 0
    while len(str(num)) > 1:  # это цикл который будет фигачить интерации до тех пор пока условия не будет выполнено.
        number_of_iterations += 1
        for i in str(num):
            work *= int(i)  # 3 итерации он перемножил числа = 24
            num = str(work)  # эту фигню я отправляю в num
        if len(num) > 1:  # смотрит что если num все ещё больше
            work = 1 # то нужно вернуть ворку 1 что бы перемножить все снова
    return number_of_iterations
