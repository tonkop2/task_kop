def string_concatenation(str1, str2):

    str3 = str1.replace(str1[0] + str1[1], str2[0] + str2[1], 1)
    str4 = str2.replace(str2[0] + str2[1], str1[0] + str1[1], 1)

    result_string = str3 + " " + str4
    return result_string

print(string_concatenation("Аапельсин", "Ггруша"))
