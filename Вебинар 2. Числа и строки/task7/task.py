def minimum_length_slice(first_string, second_string):
    x = second_string.find(first_string[0])
    y = second_string.find(first_string[1])
    z = second_string.find(first_string[2])

    minimum_figure = min(x, y, z)
    max_figure = max(x, y, z)
    min_slice = second_string[minimum_figure:max_figure + 1:]
    return min_slice