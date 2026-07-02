file=open("app.py","r")
# print(file.readable())
# print(file.read())
# print(file.readline())
# print(file.readlines())
# file.close()

from Class import Student

student1=Student("Jim",8,9,"False")
student2=Student("Kelly",9,5,"True")

print(student1.name)
print(student2.honor())