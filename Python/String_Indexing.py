# a = "Sachin"
# print(a[0])
# print("Hello"[0])

# # Connection(+)
# a="Sachin"
# b="Patel"
# full_name = a+" "+b
# print(full_name)

# # Repetation (*)
# a='Sachin'
# print(a * 30)

# # Q1. Create a string with your name. Print its length and data type.
# a="sachin patel"
# print(len(a))
# print(a, type(a))

# # Q2. Print the first and last character of the string 'DataScience'.
# a="DataScience"
# print(a[0])
# print(a[-1])

# # Q3. Using negative indexing, print the 3rd character from the end of 'PyMaster'.
# a="PyMaster"
# print(a[-3])

# # Q4. Slice 'PROGRAMMING' to extract only 'GRAM'
# a="PROGRAMMING"
# print(a[3:7])

# # Q5. Reverse the string 'India' using slicing.
# a="India"
# print(a[::-1])

# a="Sachin Patel  "
# # print(a.lower())
# # print(a.upper())
# # print(a.title())
# # print(a.strip())
# # print(a.capitalize())
# # print(a.swapcase())
# a=" one two three four "
# # print(a.split())
# # print(a.split(","))
# a=" one , two , three , four "
# print(a.split(",",2))


# # join is the INVERSE of split
# words = ['Python', 'is', 'awesome']
# print(' '.join(words)) # Python is awesome
# print('-'.join(words)) # Python-is-awesome
# print(''.join(words)) # Pythonisawesome
# # Common pattern: split → process → join
# s = 'one two three'
# words = s.split()
# upper_words = [w.upper() for w in words] # (we will cover this later!)
# result = ' '.join(upper_words)
# print(result) # ONE TWO THREE


# print("hello123".isalnum()) # True — all alphanumeric?
# print("hello".isalpha()) # True — all letters?
# print("12345".isdigit()) # True — all digits?
# print(" ".isspace()) # True — all whitespace?
# print("Hello World".istitle())# True — title case?
# print("HELLO".isupper()) # True — all uppercase?
# print("hello".islower()) # True — all lowercase?
# # startswith / endswith
# print("Python".startswith("Py")) # True
# print("Python".endswith("on")) # True
# print("Python".startswith(("Py","Go"))) # True ← accepts a tuple!


# name = "Sachin"
# score = 95.5
# # Basic usage
# print(f"Name: {name}") # Name: Sachin
# print(f"Score: {score}") # Score: 95.5
# # Expressions inside {}
# print(f"2 + 3 = {2 + 3}") # 2 + 3 = 5
# print(f"{name.upper()} rocks!") # SACHIN rocks!
# # Number formatting
# print(f"{score:.2f}") # 95.50 (2 decimal places)
# print(f"{1000000:,}") # 1,000,000 (comma separator)
# print(f"{score:.0f}%") # 96% (round to int)
# # Multi-line f-string
# card = f"""
# Student : {name}
# Score : {score:.1f}
# Grade : {"A" if score >= 90 else "B"}
# """
# print(card)

# Implement palindrome check, vowel count, and reverse string
# Palindrome check
n=input("Enter a any type of string: ")
a=n.lower()
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
if a==b:
    print(f"Palindrome String")
else:
    print(f"Not a Palindrome String")

# vowel count
n=input("Enter a any type of string: ")
a=n.lower()
vowel="aeiou"
count=0
for i in a:
    if i in vowel:
        count+=1
print(count)


# Reverse string
n=input("Enter a any type of string: ")
b=""
for i in range(len(n)-1,-1,-1):
    b+=n[i]
print(b)
