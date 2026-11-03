# # try / except — Catching Errors
# try:
#     a = int(input("Enter a :"))
#     b = int(input("Enter b :"))
    
#     z=a/b
#     print(z)
# except ZeroDivisionError as e:
#     print(f"Error : {e}")
# except ValueError as e:  
#     print(f"Error : {e}")
    
# print("Your result")



# # try / except / finally — Catching Errors
# try:
#     a = int(input("Enter a :"))
#     b = int(input("Enter b :"))
    
#     z=a/b
#     print(z)
# except ZeroDivisionError as e:
#     print(f"Error : {e}")
# except ValueError as e:  
#     print(f"Error : {e}")
# finally:
#     print("wow wow wow")
    
# print("Your result")



# # try / except / else / finally — Catching Errors
# try:
#     a = int(input("Enter a :"))
#     b = int(input("Enter b :"))
    
#     z=a/b
#     print(z)
# except ZeroDivisionError as e:
#     print(f"Error : {e}")
# except ValueError as e:  
#     print(f"Error : {e}")
# else:
#     print("No Exceptional Handling")
# finally:
#     print("wow wow wow")
    
# print("Your result")



# # raise — Triggering Your Own Errors
# def set_age(age):
#     if age < 0:
#         raise ValueError("Age is negative")
#     return age

# try:
#  a=set_age(int(input("Enter a age :")))
# except ValueError as e:
#     print("Caught:", e) 
# print(a)



# # Re-raise — Triggering Your Own Errors
# def set_age(age):
#     if age < 0:
#         raise ValueError("Age is negative")
#     return age

# try:
#  a=set_age(int(input("Enter a age :")))
# except ValueError as e:
#     print("Caught:", e) 
#     raise

# print(a)



# '''
# Safe List Access
# Given items = [10, 20, 30] , ask the user for an index and print that item. Catch
# IndexError and print "No item there" if the index is out of range.
# '''
# i=int(input("Enter a index :"))
# try:
#     items = [10, 20, 30]
#     print(items[i])
# except IndexError as e:
#     print(f"Error :{e}")
         


# '''
# Safe Dictionary Lookup
# Given a phone book dict, ask for a name and print the number. Catch KeyError
# and print "Name not found" . (Compare with using .get() from #14.)
# Hint: except KeyError .
# '''
# phone_book = {
#     "Rajeev": "9876543210",
#     "Amit":   "9123456780",
#     "Priya":  "9988776655"
# }

# name = input("Enter a name: ")

# try:
#     print(f"{name}: {phone_book[name]}")
# except KeyError:
#     print("Name not found")



# '''
# Always Say Goodbye
# Write a try/except that converts user input to int . Add a finally block that
# always prints "Thanks for using the app!" whether or not there was an error.
# Hint: add a finally block.

# '''
# phone_book = {
#     "Rajeev": "9876543210",
#     "Amit":   "9123456780",
#     "Priya":  "9988776655",
#     "Sachin": "9039271597"
# }

# name = input("Enter a name: ")

# try:
#     print(f"{name}: {phone_book[name]}")
# except KeyError:
#     print("Name not found")
# finally:
#     print("Thanks for using the app!")
    
    
def f():
    try:
        return "try"
    # except:
    #     print("Error")
    finally:
        print("finally runs")
print(f())
    
    
    