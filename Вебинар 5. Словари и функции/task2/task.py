our_str='letter'
slovarZapis = {}
slovarObhii = {}



for i in our_str:
    slovarZapis = dict.fromkeys([i], 1)
    slovarObhii.update(slovarZapis)
    print(slovarObhii) #тут вычленинл все буквы в словарь



for i in our_str:
    slovar = slovarObhii.get(i) #тут я вытаскиваю значение по ключу который приходит из слова
    slovar = int(slovar) + 1
    slovarObhii = dict.fromkeys([i], slovar)
    print(slovarObhii)

def repeats(our_str):
    """Повторы букв
    :param our_str: строка
    :return: новая строка с повторами букв
    """
    # todo Здесь нужно написать код
    return

