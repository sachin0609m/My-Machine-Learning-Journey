# # Creating a Class & Making Objects
# class myclass():  # Create Class 
#     pass

# ob=myclass()  # Creat object

# # Basic Self Use 
# class myclass():
#     def __init__(self):
#         print(f"Object Created")
#         # pass
    
#     def sum(self):
#         print(f"Sum = {6+8}")
#     def prod(self):
#         print(f"Product = {6*8}")
        
# ob = myclass()
# ob.sum()
# ob.prod()



# # With self pass arguments
# class myclass():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print(f"Object Created")
#         # pass
    
#     def sum(self):
#         print(f"Sum = {self.a+self.b}")
#     def prod(self):
#         print(f"Product = {self.a*self.b}")
        
# ob = myclass(24,6)
# ob.sum()
# ob.prod()

# ob1 = myclass(6,9)
# ob1.sum()
# ob1.prod()


# Global and Local Variable
# class myclass():
#     def __init__(self,a,b):
#         self.a=a        # Global variable a
#         self.b=b        # Global variable b
#         # print(f"Object Created")
#         # pass
    
#     def sum(self):
#         print(f"Sum = {self.a+self.b}")
#     def prod(self):
#         print(f"Product = {self.a*self.b}")
    
#     def area(self,r):       # Locial Variable r
#         pi = 3.1415         # Locial Variable pi
#         print(f"Aera = {pi*r*r}")
        
# ob = myclass(24,6)
# ob.sum()
# ob.prod()
# ob.area(24)

# ob1 = myclass(6,9)
# ob1.sum()
# ob1.prod()
# ob1.area(6)



# # Class Variable / Class Attribute
# class myclass():
#     name = "Maths Calculation"      # Class Variable / Class Attribute , Same class name will be there for different objects
#     def __init__(self,a,b):
#         self.a=a        # Global variable a
#         self.b=b        # Global variable b
#         # print(f"Object Created")
#         # pass
    
#     def sum(self):
#         print(f"Sum = {self.a+self.b}")
#     def prod(self):
#         print(f"Product = {self.a*self.b}")
    
#     def area(self,r):       # Locial Variable r
#         pi = 3.1415         # Locial Variable pi
#         print(f"Aera = {pi*r*r}")

# ob = myclass(4,5.2)
# ob1 = myclass(54,86)
# ob2 = myclass(47,69)
# ob3 = myclass(95,35)

# print(f"Class is {ob.name}")
# print(f"Class is {ob1.name}")
# print(f"Class is {ob2.name}")
# print(f"Class is {ob3.name}")



# # Create a Rectangle class with width and height. Add methods area() and perimeter().
# class Rectangle():
#     def __init__(self,h,w):
#         self.h=h
#         self.w=w
        
#     def area (self):
#         print(f"Height :{self.h}\nWidth :{self.w}")
#         print(f"Area of rectangle = {self.h*self.w}")
        
#     def peri (self):
#         print(f"Height :{self.h}\nWidth :{self.w}")
#         print(f"Perimeter of rectangle = {2*(self.h+self.w)}")

# ob = Rectangle(15,7)
# ob.area()
# ob.peri()


class student():
    school = "Sheat"
    s_name = "SVGI"
    def __init__(self,name):
        self.name=name
    
    def speak(self):      # needs an object
        print(f"Name :{self.name}")
        
    @classmethod      # needs the class
    def get_class(cls):
        print(f"School Name :{cls.s_name}")
    
    @staticmethod     # needs nothing
    def print_data():
        print("Hello!!!\n")
    
ob = student("Sachin")        # needs an object
ob.speak()
ob.print_data()       # needs nothing

ob1 = student("Parth")        # needs an object
ob1.speak()
ob1.print_data()      # needs nothing

student.get_class()       # needs the class
student.print_data()      # needs nothing        




