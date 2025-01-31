# a = (1, 2)
# b, c = a
# z = a
# print(b)
# print(c)
# print(z)

a= [1,2,3]

def nbbv(c):
    return a[0:1]

def dsfj(c):
    c.pop(1)

print(nbbv(a))
print(a)


print(dsfj(a))
print(a)



def test_file_path(file_path):
    import os

    file_name = os.path.splitext(os.path.basename(file_path))[0]
    disk_name = file_path[:1]
    root_folder1 = current_file = os.path.realpath(file_path)
    root_folder = os.path.dirname(root_folder1)[3:12]

    return file_name, disk_name, root_folder
