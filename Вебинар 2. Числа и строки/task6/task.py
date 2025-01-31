string='Hello World'
new_string = string[0::3] #0 - пропускает т.к. с него начинает H-1,e-2,l-3
print(new_string)

def delete_symbols(string):

    new_string = string[0::2] #c 0(c первой буквы) до конца(ничего нет) с шагом 2 (т.е. выбирает каждую следующую цифру начиная от скобки, 2ю он пропускает)

    return new_string
