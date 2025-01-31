podrazdelenie = ('Разработка', 'УК', 'Автотесты')
a = 32
slovar = {}  # создаем пустой словарь
podrazdelenie2 = ""


for i2 in podrazdelenie:
    podrazdelenie2 = podrazdelenie2 + i2
for i in podrazdelenie2:
    if i != " ": # i не равно пробелу
        if slovar.get(i) is None: #Проверка на вхождение в словарь, нет в словаре
            slovar.update({i: 1}) #добавляем в словарь
        else: #Проверка на вхождение в словарь, есть в словаре
            znacenie = slovar.get(i) #вытаскиваем зачение из ключа
            znacenie = znacenie + 1 #прибавляем + 1 к зачению
            slovar.update({i: znacenie}) #обновляем словарь

sortirovka = list(slovar.values()) #вычленяем только значения list преобразовывает его в список
sortirovka.sort() #сортируем от меньшего к большему
sortirovka.reverse() # меняем их местами от большего к меньшему
summaIzSortirovki = int(sortirovka[0]) + int(sortirovka[1]) + int(sortirovka[2]) #складываем

b = 1337 * a * summaIzSortirovki
print(b)

class PersonInfo:
    def __init__(self, fi, age, *deps):
        self.fi = fi
        self.age = age
        self.deps = deps

    def short_name(self):
        """Краткая запись Фамилия И."""
        familiaImia = self.fi #добавляем инфу из атрибута в переменную
        familiaImiaItog = familiaImia.split() #split() - разделяет строку на подстроки т.е. имя и фамилия имеют разные индексы
        familia = familiaImiaItog[1]
        Imia = familiaImiaItog[0]
        ItogFIO = f"{familia} {Imia[0]}."
        return ItogFIO

    def path_deps(self):
        """Путь до подразделения"""
        podrazdelenieItog = " "
        podrazdelenie = self.deps
        for i in podrazdelenie:
            if podrazdelenieItog == " ":
                podrazdelenieItog = f"{i}"
            else:
                podrazdelenieItog += f" --> {i}"
        return podrazdelenieItog

    def new_salary(self):
        """Новая зарплата"""
        podrazdelenie = self.deps
        vozrast = self.age

        slovar = {}  # создаем пустой словарь
        cifra = 1337
        podrazdelenie2 = ""

        for i2 in podrazdelenie:
            podrazdelenie2 = podrazdelenie2 + i2
        for i in podrazdelenie2:
            if i != " ":  # i не равно пробелу
                if slovar.get(i) is None:  # Проверка на вхождение в словарь, нет в словаре
                    slovar.update({i: 1})  # добавляем в словарь
                else:  # Проверка на вхождение в словарь, есть в словаре
                    znacenie = slovar.get(i)  # вытаскиваем зачение из ключа
                    znacenie = znacenie + 1  # прибавляем + 1 к зачению
                    slovar.update({i: znacenie})  # обновляем словарь

        sortirovka = list(slovar.values())  # вычленяем только значения list преобразовывает его в список
        sortirovka.sort()  # сортируем от меньшего к большему
        sortirovka.reverse()  # меняем их местами от большего к меньшему
        summaIzSortirovki = int(sortirovka[0]) + int(sortirovka[1]) + int(sortirovka[2])  # складываем

        cifraItog = cifra * vozrast * summaIzSortirovki
        return cifraItog


# a = PersonInfo('Александр Шленский',32, 'Разработка', 'УК', 'Автотесты')
# # a.vremia()
# # PersonInfo.vremia()
# # PersonInfo('Александр Шленский',32, 'Разработка', 'УК', 'Автотесты').path_deps()
# print(a.new_salary())