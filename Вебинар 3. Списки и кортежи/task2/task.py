def get_list_info(lst):

    min_elem = min(lst)
    max_elem = max(lst)
    sum_list = sum(lst)
    average = sum(lst) / len(lst)
    average = round(average, 2)

    tuple = min_elem, max_elem, sum_list, average
    return tuple
