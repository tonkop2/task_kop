cats_data=[('Мартин', 5, 'Алексей', 'Егоров'),
         ('Фродо', 3, 'Анна', 'Самохина'),
         ('Вася', 4, 'Алексей', 'Егоров')]
spisok2 = {}
obhii2 = ""


for i in cats_data: #перебираем кортеджи
    cats_data2 = i #записываем кортедж который нам попался в переменную
    klichka_vosrast = f"{cats_data2[0]}, {cats_data2[1]}" #кличка и возраст (тут список)
    imia_familia = f"{cats_data2[2]} {cats_data2[3]}:" #тут фио (тут строка)
    if spisok2.get(imia_familia) is None:  # через is а не == делай в другой раз
        spisok2.update({imia_familia: [klichka_vosrast]})  # тут все это записываем полный список ключ + значение

    else:
        spisok2[imia_familia].append(klichka_vosrast)  #тут берём уже сущействующий ключ и обновляем через append значение

for key, item in spisok2.items():  # получение списка вида (ключ, значение)
    klichkastr = '; '.join(item)
    obhii = f"{key} {klichkastr}"
    obhii2 = f"{obhii2}\n{obhii}"

    print(obhii2)





def everything_for_your_cat(cats_data):
        spisok2 = {}
        for i in cats_data: #перебираем кортеджи
            cats_data2 = i #записываем кортедж который нам попался в переменную
            klichka_vosrast = f"{cats_data2[0]}, {cats_data2[1]}" #кличка и возраст (тут список)
            imia_familia = f"{cats_data2[2]} {cats_data2[3]}:" #тут фио (тут строка)
            if spisok2.get(imia_familia) is None:  # через is а не == делай в другой раз
                spisok2.update({imia_familia: [klichka_vosrast]})  # тут все это записываем полный список ключ + значение

            else:
                spisok2[imia_familia].append(klichka_vosrast)  #тут берём уже сущействующий ключ и обновляем через append значение

        for key, item in spisok2.items():  # получение списка вида (ключ, значение)
            klichkastr = '; '.join(item)
            obhii = f"{key} {klichkastr}"

        return obhii
