spisokCifr = '0123456789'
spisok = ""
with open("test_file/task1_data.txt", 'r', encoding='utf-8') as file:
    lines = file.read()
    for ii in lines: #перебираем по буквам
        if not ii.isdigit(): #смотрим есть ли цифра если нет то записываем в строку
            spisok += ii
    print(spisok)
with open("test_file/task1_answer.txt", "w", encoding='utf-8') as file2: #создаем новый файл
    file2.write(spisok)
