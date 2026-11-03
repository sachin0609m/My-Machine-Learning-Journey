# # open() and File Mode Write
# file = open("data.txt","w")

# file.write("Hello I am Sachin.\n")
# file.write("I am a Machine Learning Engineer.\n")

# lines = ["apple\n", "banana\n", "cherry\n"]
# file.writelines(lines) # writes them all

# file.close()


# # Append mode
# file = open("data.txt","a")
# file.write("B.Tech Information Technology Job Roles\n")
# roles = ["Machine Learning Intern\n","Data Science Intern\n","Data Analyst Intern\n","Python Developer Intern\n"]
# file.writelines(roles)
# file.close()


# Reading from a File
file=open("data.txt","r")

# content = file.read()  # All line read in file
# print(content)

# content = file.readline()  #Only single line read in file
# print(content)

# content = file.readlines()  #All line read in a list form
# print(content)

# for line in file:
#     print(line.strip())
#     #output:Hello I am Sachin.
#         #   I am a Machine Learning Engineer.
#         #   B.Tech Information Technology Job Roles
#         #   Machine Learning Intern
#         #   Data Science Intern
#         #   Data Analyst Intern
#         #   Python Developer Intern
# file.close()


# # With statement
# with open("data.txt","r") as file:
#     content = file.readline()
#     print(content)


# # Handling File Errors
# try:
#     with open("missing.txt", "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("That file doesn't exist!")
# except PermissionError:
#     print("No permission to open it.")
    

# try:
#     with open("data.txt", "r") as file:
#         print(file.writelines())
# except FileNotFoundError:
#     print("That file doesn't exist!")
# except PermissionError:
#     print("No permission to open it.")
# except TypeError as e:
#     print("Error:",e)


# with open("data.txt","r") as file:
#     x=file.readlines()
#     print(len(x))
    
    # count=0
    # for line in file:
    #     count+=1
    # print("Total line in file is ",count)  

 
# with open("data.txt","r") as file:
#     for line in file:
#         print(f"Total words in line :",len(line.split()))  




# with open("data12.txt", "w") as f:
#  f.write("hello\n")
with open("data12.txt", "a") as f:
 f.write("worl")
