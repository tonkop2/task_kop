class Trigon:
    w = {}
    def __init__(self, *args):
        self.args = args
        self.check_arks_corret(self.args)
    # статикметод он говорит, что данная функция является фукцией класса, и записывает данные в sides
    # в sides данные которые он записывет он тянет эти данные из self.check_arks_corret(self.args)
    # именно данные - которые он сможет записать в sides т.е. sides - пустая переменная без данных
    # в которую нужно записать данные. Просто на переменную ты ссослаться не можешь.
    # Т.к. он ждёт получение данных которые ему нужно записать в sides
    @staticmethod
    def check_arks_corret(sides):

        for i in sides:
            if not isinstance(i, int):
                raise TypeError('Стороны должны быть числами')
            if i <= 0:
                raise ValueError('Стороны должны быть положительными')

        #колличество символов
        if len(sides) != 3:
            raise IndexError(f'Передано {len(sides)} аргументов, а ожидается 3')

        #неравенство треугольника
        if sides[0]+sides[2] <= sides[1] or \
                sides[1]+sides[2] <= sides[0] or \
                sides[0]+sides[1] <= sides[2]:
            raise Exception ('Не треугольник')




# a = Trigon
# b = Trigon(2,2,3)
# print()




# programList = (1, 1, 2)
# obheecislo = ""
#
#
# if programList[0] == programList[1] or programList[1] == programList[2]:
#     print("равно")
# else:
#     print("не равно")








