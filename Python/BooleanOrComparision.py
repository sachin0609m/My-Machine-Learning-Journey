# # Boolean
# is_online = True
# is_admin = False
# print(type(is_online)) # <class 'bool'>

# winner = None # no winner decided yet
# print(winner) # None


# # Comparision operators
# marks = 72
# print(marks >= 40) # True (passed)
# print(marks == 100) # False
# name = "Rajeev"
# print(name == "Rajeev") # True — works on text too


# # Logic Operators
# age = 20
# has_id = True
# # both must be true to enter
# print(age >= 18 and has_id) # True
# # any one true is enough
# print(age < 13 or has_id) # True
# print(not has_id) 


# Truthy & Falsy Values
name = ""
if name:
    print("Hello")
else:
    print("Name is empty") # this runs — "" is falsy
items = [1, 2]
if items:
    print("Cart has items") # runs — non-empty list is truthy





