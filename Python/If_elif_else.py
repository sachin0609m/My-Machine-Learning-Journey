# x = 5 
# if 10>x>3:
#     print ("Yes")
# else:
#     print ("No")
    
    

# age = 20
# if age < 13:
#     print("You are a child")
# elif age < 20:
#     print("You are a teenager")
# elif age < 60:
#     print("You are an adult")
# else:
#     print("You are a senior citizen")


num = float(input("Enter a any type or number :"))

if num>0:
    print(f"This is a Positive integer")
elif num<0:
    print(f"This is a Negative integer")
else:
    print(f"This is a Zeros")


num = float(input("Enter a any type or number :"))
if num%2==0:
    print(f"This is a Even Number")
else:
    print(f"This is a odd Number")


marks = 75
# normal way
if marks >= 33:
    result = "Pass"
else:
    result = "Fail"
# one-line way (same thing)
result = "Pass" if marks >= 33 else "Fail"
print(result)


# match-case (Python 3.10+ Switch)
day = "SUN"
match day:
    case "MON":
        print("Start of the week")
    case "SAT" | "SUN":
        print("Weekend!")
    case _:
        print("A normal day")
