import math #что бы корень квадратный сработал, нужна эта библиотека
class Segment:
    def __init__(self, first_point, second_point): #__init__() - конструктор. Конструктору также необходимо передать специальный параметр — self. Параметр self ссылается на экземпляр объекта. Присваивание этого ключевого слова означает, что атрибут попадает в экземпляр объекта.
        self.first_point = first_point
        self.second_point = second_point

    def length(self):
        x1, y1 = self.first_point #инициализируем, что будет в аргументах, какие значения
        x2, y2 = self.second_point #инициализируем, что будет в аргументах, какие значения
        znacenie = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2) #math.sqrt - извлекаем корень квадратный, round округляем(2ка в конце это 2 знака после запятой) ** возведение в степень
        return znacenie

    def x_axis_intersection(self):
        """Пересечение оси абсцисс"""
        x1, y1 = self.first_point  # инициализируем, что будет в аргументах, какие значения
        x2, y2 = self.second_point  # инициализируем, что будет в аргументах, какие значения

        if y1 == 0 and y2 == 0:
            return True
        if min(y1, y2) < 0 < max(y1, y2): 
            return True
        else:
            return False

    def y_axis_intersection(self):
        """Пересечение оси ординат"""
        x1, y1 = self.first_point  # инициализируем, что будет в аргументах, какие значения
        x2, y2 = self.second_point  # инициализируем, что будет в аргументах, какие значения
        if x1 == 0 and x2 == 0:
            return True
        if min(x1, x2) < 0 < max(x1, x2):
            return True
        else:
            return False

