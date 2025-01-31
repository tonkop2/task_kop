def treatment_sum(our_tuple):
    """Обработка суммы элементов кортежа
    :param our_tuple: кортеж
    :return: сумму элементов кортежа
    """
    # todo Здесь нужно написать код
    try:
        if len(our_tuple) > 2:
            raise AssertionError('Много данных')
        resultat = our_tuple[0] + our_tuple[1]
        return resultat
    except TypeError:
        return 'Нельзя сложить эти данные'
    except IndexError:
        return 'Недостаточно данных'
    except AssertionError:
        raise Exception('Много данных')
    except Exception as e:
         print(e)


treatment_sum((1,2))




