# def intro (id,name,age,salary):
#     print(f"ID : {id}")
#     print(f"Name is {name}") 
#     print(f"Age : {age}")
#     print(f"Salary : {salary}")
    
# intro(1103,'Sachin',22,60000)
# print("_"*30)
# intro(4571,"Nupur",26,70000)
    
    
    
# # Positional vs keyword arguments    
# def profile(name, age):
#  print(name, "is", age)
# # positional — order matters
# profile("Amit", 21) # Amit is 21
# # keyword — name them, order doesn't matter
# profile(age=21, name="Amit") # Amit is 21



# # Default arguments /Default arguments must come AFTER non-default ones. def f(msg="hi", name) is an error.
# def greet(name, msg="welcome"):
#  print(name, msg)
# greet("Amit") # Amit welcome (default used)
# greet("Neha", "hello") # Neha hello (override)



# # Area of rectangle 
# def Area(l,b):
#     area = l*b
#     return area

# Area_of_rectangle = Area(24,6)
# print(Area_of_rectangle)
    


# """
# Is Even?
# Write a function is_even(n) that returns True if n is even, else False . Test it
# with a few numbers.
# Hint: return n % 2 == 0
# """
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# print(is_even(int(input("Enter a number: "))))
    
    

# '''
# Simple Interest
# Write a function interest(principal, rate, years) that returns the simple
# interest ( P * R * T / 100 ). Give rate a default of 5. Call it once using the
# default and once overriding it.
# Hint: return the formula; use a default argument for rate
# '''
# def interest(P,T,R=5):
#     print( P * R * T / 100 )

# interest(60000,5)



# def biggest(a, b, c):
#     if a>b and a>c:
#         print("Biggest : ",a)
#     elif b>a and b>c:
#         print("Biggest : ",b)
#     else:
#         print("Biggest : ",c)   
        
# biggest(457,524,145) 



# # Local vs Global Scope
# def show():
#  x = 10 # local — lives only inside show()
#  print(x)
# show() # 10
# # print(x) # NameError — x doesn't exist out here


# msg = "global" # global — visible everywhere
# def read():
#  print(msg) # can READ the global
# read() # global



# count = 0
# def bump():
#  count = count + 1 # UnboundLocalError!
# # better: take input, return output — no globals
# def bump(count):
#  return count + 1
# count = bump(count) # clean and predictable


# # The LEGB Rule
# x = "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         x = "local"
#     print(x) # finds Local first
#     inner()
# outer() # local


# # Docstrings — Documenting Your Function
# def average(marks):
#  """Return the average of a list of marks."""
#  return sum(marks) / len(marks)
# # read it back anytime
# print(average.__doc__) # Return the average of a list of marks.
# help(average) # shows the docstring too

# import Avg_Function as x
# a=int(input("Enter a number : "))
# b=int(input("Enter a number : "))
# c=int(input("Enter a number : "))

# print(x.avg(a,b,c))

# import Average as av
# m=24
# n=6
# print("Add : ",av.add(m,n))
# print("Average : ",av.avg(m,n))
# print("Product : ",av.prod(m,n))


# from Average import prod
# m=2424
# n=6
# print(prod(m,n))




# import OOP as op
from OOP import myclass
ob = myclass(5427,54)
ob.sum
ob.prod
ob.area(9)

ob1 = myclass(963,852)
ob1.sum()
ob1.prod()
ob1.area(19)





