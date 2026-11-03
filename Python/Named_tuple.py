# # The Problem with Plain Tuples
# student = ("Amit", 21, "BCA", 8.5)
# print(student[0]) # Amit ... but was index 3 gpa or age?
# print(student[3]) # 8.5 ... you have to remember!



# # Creating a Named Tuple
# from collections import namedtuple
# # define the shape: a name + its fields
# Student = namedtuple("Student", ["name", "age", "course", "gpa"])
# # create a record
# s = Student("Sachin", 22, "B.Tech", 8.5)
# print(s.name) # Sachin (access by name!)
# print(s.gpa) # 8.5
# print(s[0]) # Sachin (still works like a tuple)
# l1 = ["Nupur", 25 , "PHD" , 9.9]
# s2 = Student._make(l1)
# print(s2.name) 
# print(s2.gpa) 
# print(s2[0])


# # fields can also be given as a single space-separated string
# Point = namedtuple("Point", "x y")
# p = Point(10, 20)
# print(p.x, p.y) # 10 20


from collections import namedtuple
Student = namedtuple ( 'Student' ,['name' , 'age' , 'gpa'] )
rows = [["Amit", 21, 8.5], 
        ["Neha", 20, 9.1], 
        ["Ravi", 22, 7.8]]
s1 = Student._make(rows)
print(s1.name)
students = [Student._make(row) for row in rows]
for student in students:
    print(student.name, student.age, student.gpa)





