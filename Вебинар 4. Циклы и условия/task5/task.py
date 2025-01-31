#строим список из цифры которую нам дали выше в num_people
def josephus_task(num_people, kill_num):
    people = []
    for i in range( 1, num_people +1): #range создает последовательность чисел
        people.append(i) #заполняет список через append + 1 что бы сдвинул цифру на 1 вперёд

    #тут рубим народ как сказано в задаче
    while len(people) > 1: #чекаем сколько людей у нас есть
        leftovers = (kill_num -1) % len(people) # тут мы берём остаток от деления 6 % 4 = 2 (2 остаток) ( -1 потомучт , индекс нам нужен 2 ибо начинается 0, 1, 2)
        del people[leftovers] #удаляет элемент по индексу
        people = people[leftovers:] + people[: leftovers] #тут над доделать
        print(leftovers)
        print(people)
    return people[0]


# for LivingPeople in range(kill_num, len(people), kill_num): #тут мы вытягиваем цифры мы будем удалять(3, колличество цифр, шаг 3)
     #тут с помощью поп удаляю цифры которые мне выдал цикл
# spisok = list(range(1, num_people + 1)) #строим список

#   тут считает правильно

# last = 0
#
# for i in range(1, num_people + 1):
#     last = (last + kill_num) % i
# print(last + 1)



    # if len(spisok) >= 7:
    #     people = (num_people + kill_num -1) % len(spisok)
    #     spisok.pop(people)
    #     print(spisok)
    # if len(spisok) == 6 or len(spisok) <= 2:
    #     people = (num_people + kill_num) % len(spisok)
    #     spisok.pop(people)
    #     print(spisok)
    # if len(spisok) > 2:
    #     people = (num_people + kill_num + 1) % len(spisok)
    #     spisok.pop(people)
    #     print(spisok)

def josephus_task2(num_people, kill_num):
    last = 0
    for i in range(1, num_people + 1):
        last = (last + kill_num) % i

    return (last + 1)
