# # Creating Dictionaries 
# # literal — the most common way
# student = {"name": "Sachin", 
#            "age": 21, 
#            "gpa": 8.5}
# print(student)

# # empty dict
# empty = {}

# # using the dict() constructor
# person = dict(name="Neha", city="Varanasi")
# print(person) # {'name': 'Neha', 'city': 'Varanasi'}

# # from a list of pairs
# pairs = dict([("a", 1), ("b", 2)])
# print(pairs) # {'a': 1, 'b': 2}
# # pairs = dict([("a", 1 ,'s', 6), ("b", 2 , 'n', 24)]) # Does not possible
# # print(pairs)



# place = {
#     "Indore" : 7,
#     "Pune" : 8,
#     "Mhow" : 10,
#     "Pithamput" : 6
# }
# print(place)
# print(place["Mhow"])

# d1 = {
#     1 : "Sachin",
#     2 : "Parth",
#     3 : "Ravina",
#     4 : "Aditi",
#     5 : {
#         'a' : "Anshul",
#         'p' : "Pardumn",
#         'a2' : "Ayush",
#         'd' : "Devendra"
#     }
# }

# print(d1)
# print(d1[5])
# new_d = d1[5]
# print(new_d['a'])


# # Read
# student = {"name": "Amit", "age": 21}
# print(student["name"]) # Amit
# # print(student["email"]) # KeyError! key doesn't exist
# # get() returns None (or a default) instead of crashing
# print(student.get("email")) # None
# print(student.get("email", "N/A")) # N/A

# # Add & Update
# student = {"name": "Amit", "age": 21}
# student["gpa"] = 8.5 # ADD a new key
# student["age"] = 22 # UPDATE existing key
# print(student) # {'name':'Amit','age':22,'gpa':8.5}


# # Delete
# student = {"name": "Amit", "age": 22, "gpa": 8.5}
# del student["gpa"] # remove a key
# age = student.pop("age") # remove AND return the value
# print(age) # 22
# print(student) # {'name': 'Amit'}


# #  Looping Over a Dictionary
# student = {
#     "name": "Sachin",
#     "age": 21,
#     "gpa": 8.5,
#     "city": "Indore",
#     "course": "B.Tech",
#     "branch": "Information Technology",
#     "college": "SVCE",
#     "year": 2026,
#     "gender": "Male",
#     "email": "sachiin@example.com",
#     "phone": "9876543210",
#     "skills": "Python",
#     "hobby": "Badminton",
#     "attendance": 85,
#     "is_placed": False
# }

# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())

# for key in student:
#  print(key)

# for k in student.keys():
#     print(student[k])     

# for ele in student.values():
#     print(ele)



# for k,v in student.items():
#     print(f'{k}:{v}')


# #  defaultdict & Counter
# from collections import defaultdict
# # count letters — the messy normal-dict way
# counts = {}
# for ch in "banana":
#     if ch in counts:
#         counts[ch] += 1
#     else:
#         counts[ch] = 1

# # the clean defaultdict way
# counts = defaultdict(int) # missing keys start at 0
# for ch in "banana":
#  counts[ch] += 1
# print(dict(counts)) # {'b': 1, 'a': 3, 'n': 2}


# '''
# Print a Price List
# Given prices = {"pen": 10, "book": 50, "bag": 200} , loop over it with
# .items() and print each line as "pen costs 10" .
# Uses: .items() looping
# '''
# prices = {
#     "pen": 10, 
#     "book": 50, 
#     "bag": 200
#     }
# for k,v in prices.items():
#     print(f'{k} costs {v}')


'''
Total & Highest
Given marks = {"math": 90, "sci": 85, "eng": 78} , use looping to print the
total marks and the subject with the highest marks.
'''
marks = {"Math": 90, "Science": 85, "English": 78}

total_marks = 0
for ele in marks.values():
    total_marks +=ele
print(f"Total marks is {total_marks}")

sub = None
mar = 0
for k,v in marks.items():
    if v>mar:
        mar=v
        sub=k
print(f"Subject : {sub} and Mark : {mar}")




"""
Build a phone book dict with 3 name → number entries. Ask the user for a name
and print the number using .get() so a missing name prints "Not found"
instead of crashing.
Hint: book.get(name, "Not found")
"""
phone_book = {
    "Rajeev": "9876543210",
    "Amit":   "9123456780",
    "Priya":  "9988776655"
}

name = input("Enter a name to search: ")

number = phone_book.get(name, "Not found")

print(f"{name}: {number}")