class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        pass
        # todo Здесь нужно написать код

    def info(self):
        """Информация о транспорте"""
        # todo Здесь нужно написать код
        return


class Bus(PublicTransport):
    __z = 101

    def __init__(self):
        self._z = 10

        print()



    # def __init__(self, brand, engine_power, year, color, max_speed, passengers, car_park, fare):
    #     super().__init__(brand, engine_power, year, color, max_speed)
    #     pass
    #     # todo Здесь нужно написать код

    def park(self):
        a = self.__z
        """Парк приписки автобуса"""
        # todo Здесь нужно написать код
        return




class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        # todo Здесь нужно написать код

    def how_long(self):
        """Время прохождения маршрута"""
        # todo Здесь нужно написать код
        return


Bus()._z
Bus().park()
print()