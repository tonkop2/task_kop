# roman_num = 3263
# cifraRacurse = ""
# for i in str(roman_num)[-1: :-1]:
#     cifraRacurse += i
# if roman_num == int(cifraRacurse):
#     print(True)
# else:
#     print(False)
# print(cifraRacurse)
#
# chislo = "MMMCCLIX"
# slovar_rim = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# chifra_obhee = 0
# znachenie_promehutok = 0
#
# for i in range(len(chislo)): #перебирает индексы
#     if slovar_rim.get(chislo[i]): #обращается к словарю
#         if i == len(chislo) - 1 or slovar_rim[chislo[i]] >= slovar_rim[chislo[i + 1]]:
#             chifra_obhee += slovar_rim[chislo[i]] - znachenie_promehutok
#             znachenie_promehutok = 0
#         else:
#             znachenie_promehutok = slovar_rim[chislo[i]]
# print(chifra_obhee)



class RomanNums:

    def __init__(self, roman_num):
        self.roman_num = roman_num
        self.chifra_obhee = self.from_roman() #объявляем переменную в классе которая у нас выполняется в функции from_roman

    def from_roman(self):
        chislo = self.roman_num
        slovar_rim = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        chifra_obhee = 0
        znachenie_promehutok = 0

        for i in range(len(chislo)):  # перебирает индексы
            if slovar_rim.get(chislo[i]):  # обращается к словарю
                if i == len(chislo) - 1 or slovar_rim[chislo[i]] >= slovar_rim[chislo[i + 1]]:
                    chifra_obhee += slovar_rim[chislo[i]] - znachenie_promehutok
                    znachenie_promehutok = 0
                else:
                    znachenie_promehutok = slovar_rim[chislo[i]]
        return chifra_obhee

    def is_palindrome(self):
        cifraRacurse = str(self.chifra_obhee)[::-1]
        if self.chifra_obhee == int(cifraRacurse):
            return True
        else:
            return False

b = RomanNums('D')

b.is_palindrome()
print()
# print(b.is_palindrome)