num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
num_tuple1 = list(num_tuple) #преобразуем его в список
numburs2 = ""
(s1, s2, s3, s4, s5, s6, *s7) = num_tuple1 #распаковываем его нам нужны первые 3 цифры и следующие 3 цифры

numburs = "(" + str(s1) + str(s2) + str(s3) + ")" + " " + str(s4) + str(s5) + str(s6) + "-" #тут делаем цепочку из первых 6 цифр

for i in s7:
    numburs2 += str(i) #тут собираем последние цифры которые остались в строку

numburs3 = numburs + numburs2 #все собираем вместе

print(numburs3)
#
# num_tuple1 = str(num_tuple1)
# print(num_tuple1)

def create_phone_number(num_tuple):
    num_tuple1 = list(num_tuple) #преобразуем его в список
    numburs2 = ""

    (s1, s2, s3, s4, s5, s6, *s7) = num_tuple1 #распаковываем его нам нужны первые 3 цифры и следующие 3 цифры
    numburs = "(" + str(s1) + str(s2) + str(s3) + ")" + " " + str(s4) + str(s5) + str(s6) + "-" #тут делаем цепочку из первых 6 цифр

    for i in s7:
        numburs2 += str(i) #тут собираем последние цифры которые остались в строку

    numburs3 = numburs + numburs2 #все собираем вместе
    return numburs3
