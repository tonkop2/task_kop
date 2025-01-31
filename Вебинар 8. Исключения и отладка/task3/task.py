def segment(first_point, second_point):
    try:
       samma = first_point[0] + first_point[1] + second_point[0] + second_point[1]
       return samma

    except Exception as e:
        reversOhibka = str(e)
        return reversOhibka[::-1]

first_point = ("a", 3)
second_point = (4, 5) #14

try:
   samma = first_point[0] + first_point[1] + second_point[0] + second_point[1]
   print(samma)

except Exception as e:
    print(e)

#can only concatenate str (not "int") ot str