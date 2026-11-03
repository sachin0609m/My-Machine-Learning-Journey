# point = (10, 20)
# colors = ("red", "green", "blue")
# print(point[0]) # 10 (indexing works like a list)
# print(colors[-1]) # blue


# # Tuples are immutable
# point = (10, 20)
# point[0] = 99 # ERROR!
# TypeError: 'tuple' object does not support item assignment


# # Packing — putting values into a tuple
# person = "Sachin",22,"Pune"
# print(person) 


# # Unpacking — pulling values out
# name, age, city = person
# print(name) # Sachin
# print(city) # Pune
# # The classic: swap two variables with no temp!
# a, b = 1, 2
# a, b = b, a
# print(a, b) # 2 1
# # Star unpacking — grab the rest
# first, *rest = (1, 2, 3, 4)
# print(first, rest) # 1 [2, 3, 4]

# _________________________________________________________________________________________

# # Sets
# empty_Set = set()
# print(type(empty_Set))

# nums = {1, 2, 2, 3, 3, 3}
# print(nums) # {1, 2, 3} duplicates gone!
# # Remove duplicates from a list instantly
# items = [1, 2, 2, 3, 4, 4, 5]
# items = list(set(items))
# print(items) # [1, 2, 3, 4, 5]



# # Adding & removing
# s1={1,2,3}

# s1.add(4)
# print(s1)

# s1.remove(3)
# print(s1)

# s1.discard(24)
# print(s1)



# # Set operations — union, intersection, difference
# s1={1,2,3,4,5,6}
# s2={2,4,8,9,7,6}
# print(s1|s2)
# print(s1&s2)
# print(s2-s1)
# print(s1^s2)




# # frozenset — the immutable set
# s1=frozenset({1,2,3,4,5,6})
# print(type(s1))
# # s1.add(7) # Error
# print(s1)




# '''Remove Duplicates with a Set
# Given nums = [4, 1, 2, 2, 3, 4, 5, 1] , use a set to get only the unique
# numbers, then print how many unique numbers there are.
# Uses: set() + len()
# '''
# nums = [4, 1, 2, 2, 3, 4, 5, 1]
# new_nums = list(set(nums))
# print(new_nums)
# print(len(new_nums))



# '''
# Unpack a Student Record
# You have a tuple student = ("Amit", 21, "BCA", 8.5) = name, age, course, cgpa.
# Unpack it into four variables in one line and print a sentence: "Amit (21) studies
# BCA with GPA 8.5" .
# '''
# student = ("Amit", 21, "BCA", 8.5)
# name, age, course, cgpa = student
# print(f"{name} ({age}) studies {course} with {cgpa}")



# '''
# Two people's friend lists: a = {"Ravi", "Sara", "Deep", "Amit"} and b =
# {"Sara", "Amit", "Neha"} . Print their common friends and all friends combined.
# Hint: intersection ( & ) for common, union ( | ) for combined.
# '''
# a = {"Ravi", "Sara", "Deep", "Amit"}
# b = {"Sara", "Amit", "Neha"}
# print(a&b)
# print(a|b)



# '''
# Swap Without a Temp Variable
# Take two numbers from the user and swap their values using tuple unpacking (no
# third variable). Print before and after.
# '''
# a = int(input("Enter a first number:"))
# b = int(input("Enter a first number:"))
# print(f"Before Swap A={a} , B={b}")
# a , b= b , a
# print(f"After Swap A={a} , B={b}")



# '''
# Unique Words Counter
# Take a sentence from the user. Split it into words and print how many unique
# words it contains (ignore repeats).
# '''
# sentence = input("Enter a sentence or ignor repeats:")
# new_set= set(sentence.split())
# print(new_set)
# print(len(new_set))



# '''
# Who Dropped Out?
# registered = {"A", "B", "C", "D", "E"} signed up, but attended = {"A", "C",
# "E"} showed up. Use set difference to find who did NOT attend.
# Hint: registered - attended
# '''
# registered = {"A", "B", "C", "D", "E"}
# attended = {"A", "C", "E"}
# Not_Attend = registered-attended
# print(f"Did not attend {Not_Attend}")



# '''
# Create a list and a set both containing numbers 0 to 999999. Check if 999999 is
# present in each. Using the time module, measure and compare how long each
# lookup takes. Explain the result in a comment.
# Hint: import time , record time.time() before and after each lookup. You'll see the O(1) vs
# O(n) difference for real.
# '''
# import time

# # Create a List and a Set with numbers from 0 to 999999
# numbers_list = list(range(1000000))
# numbers_set = set(range(1000000))

# target = 999999

# # List searching
# start = time.perf_counter()
# found_in_list = target in numbers_list
# end = time.perf_counter()

# list_time = end - start

# # Set searching
# start = time.perf_counter()
# found_in_set = target in numbers_set
# end = time.perf_counter()

# set_time = end - start

# # Display results
# print("----- SEARCH RESULTS -----")
# print(f"Found in List: {found_in_list}")
# print(f"Found in Set:  {found_in_set}")

# print("\n----- SEARCHING TIME -----")
# print(f"List Time: {list_time:.8f} seconds")
# print(f"Set Time:  {set_time:.8f} seconds")

# if set_time > 0:
#     speed = list_time / set_time
#     print(f"\nSet is approximately {speed:.0f}x faster than List")



# Find the second-largest number.
s1 = (24,12,19,6,42)
largest = float("-inf")
second_largest = float("-inf")
for i in s1:
    if i>largest:
        second_largest = largest
        largest = i 
    elif i>second_largest and i<largest:
        second_largest=i
print(f"Largest = {largest}")
print(f"Second Largest = {second_largest}")


