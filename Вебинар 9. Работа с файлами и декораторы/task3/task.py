slovarObhii = {}

def memorize(function):
    def wrapper(*args):
        #тут обычно пишут то что до фунции используется
        resultat = function(*args) #итог того, что мы получили в функции
        slovar = {args: resultat} #тут обычно пишут то что после выполнения функции происходит
        if args not in slovarObhii.keys(): #смотрю что данных нет в словаре, по ключу.
            slovarObhii.update(slovar) #добавляем данный кортедж в словарик
            keshirovanie = (resultat, slovarObhii) #добавляем данные в кеш
        else:
            keshirovanie = (resultat, slovarObhii) #оставуляем все как есть
        return keshirovanie
    return wrapper


# def memorize(function):
#     kcech = {}
#     def wrapper(*args):
#         if args in kcech:
#             resultat = kcech[args]
#         else:
#             resultat = function(*args) #итог того, что мы получили в функции
#             kcech.update({args: resultat})
#         return resultat, kcech #фунция если возращает несколько значений, возвращает их кортеджем
#     return wrapper


# todo Здесь ничего изменять не нужно!
@memorize
def get_kinetic_energy(weight, speed):
    """Кинетическая энергия
    :param weight: масса
    :param speed: скорость
    :return: кинетическую энергию
    """
    return (weight * speed ** 2)/2



asd = get_kinetic_energy(5, 2)
print(asd)

asd = get_kinetic_energy(5, 3)
print(asd)

asd = get_kinetic_energy(5, 4)
print(asd)

asd = get_kinetic_energy(5, 3)
print(asd)