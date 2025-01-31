def global_function():
    """Нелокальные изменения
    :return: msg
    """
    msg = 1

    def local_function():
        pass
        # todo Здесь нужно написать код

    return msg
