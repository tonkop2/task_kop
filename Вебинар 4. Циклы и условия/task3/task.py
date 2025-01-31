num1 = "Рудик"
for i in num1:
 print(i)



def sum_digits(num):
    s = str(num)

    for i, element in enumerate(s):
        if i == 0:
            s0 = s[0]
            s10 = int(s0)
        elif i == 1:
            s1 = s[1]
            s10 = int(s0) + int(s1)
        elif i == 2:
            s2 = s[2]
            s10 = int(s0) + int(s1) + int(s2)
        elif i == 3:
            s3 = s[3]
            s10 = int(s0) + int(s1) + int(s2) + int(s3)
        elif i == 4:
            s4 = s[4]
            s10 = int(s0) + int(s1) + int(s2) + int(s3) + int(s4)
        elif i == 5:
            s5 = s[5]
            s10 = int(s0) + int(s1) + int(s2) + int(s3) + int(s4)+ int(s5)
        elif i == 6:
            s6 = s[6]
            s10 = int(s0) + int(s1) + int(s2) + int(s3) + int(s4)+ int(s5)+ int(s6)
        elif i == 7:
            s7 = s[7]
            s10 = int(s0) + int(s1) + int(s2) + int(s3) + int(s4)+ int(s5)+ int(s6)+ int(s7)
        elif i == 8:
            s8 = s[8]
            s10 = int(s0) + int(s1) + int(s2) + int(s3) + int(s4)+ int(s5)+ int(s6)+ int(s7)+ int(s8)
        elif i == 9:
            s9 = s[9]
            s10 = int(s0) + int(s1) + int(s2) + int(s3) + int(s4)+ int(s5)+ int(s6)+ int(s7)+ int(s8)+ int(s9)
    return s10



def sum_digits2(num):
    s = str(num)
    len_str = len(s)
    sum = 0
    for i in range(len_str):
        razriad = num // (10**(len_str-1 - i))
        razriad = razriad % 10
        sum +=razriad
    return sum


print(sum_digits2(12361565146))