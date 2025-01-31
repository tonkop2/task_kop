file_path = "test_file/task_2.txt"
samma_peremennoi = 0
spisok_ = []
stroki_provaerka_new = []

with open(file_path, 'r', encoding='utf-8') as file:
    stroki_provaerka_new = file.readlines() #построчно вытягивает инфу из списка

    for i in stroki_provaerka_new:
        stroki = i.replace("\n", "")  # замена переноса строки на просто пустоту в строке
        if stroki: #принцип - это если в строке есть что-то - тру, если пусто - фолс
            stroki_int = int(stroki) #меняем значение со строки на цифру
            samma_peremennoi += stroki_int #прибовляем данную цифру к общему списку
        else:
            spisok_.append(samma_peremennoi) #добавление элемента в список
            samma_peremennoi = 0
    spisok_.sort(reverse=True)
    samma_treh_zneenii = spisok_[0] + spisok_[1] + spisok_[2]
    print(samma_treh_zneenii)

def three_most_expensive_purchases():
    file_path = "test_file/task_2.txt"
    samma_peremennoi = 0
    spisok_treh_znahenii = [0, 0, 0]
    stroki_provaerka_new = []

    with open(file_path, 'r', encoding='utf-8') as file:
        stroki_provaerka_new = file.readlines()  # построчно вытягивает инфу

        for i in stroki_provaerka_new:
            stroki = i.replace("\n", "")  # замена переноса строки на просто пустоту в строке
            if stroki:  # принцип - это если в строке есть что-то - тру, если пусто - фолс
                stroki_int = int(stroki)  # меняем значение со строки на цифру
                samma_peremennoi += stroki_int  # прибовляем данную цифру к общему списку
            else:
                min_znacene = min(spisok_treh_znahenii)  # вычисляем минимальное щначение
                if (min_znacene < samma_peremennoi):  # если минимальное значение меньше того что нам пришло
                    index_ = spisok_treh_znahenii.index(min_znacene)  # вычисляем индекс этого значения
                    spisok_treh_znahenii[index_] = samma_peremennoi  # меняем это значение(минимальное) на новое
                samma_peremennoi = 0


        samma_treh_zneenii = spisok_treh_znahenii[0] + spisok_treh_znahenii[1] + spisok_treh_znahenii[2]
        most_expensive_purchases = samma_treh_zneenii
    return most_expensive_purchases
