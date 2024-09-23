"""
Michael Villavicencio
Sep 23, Python Files
"""
fileusers = open("/Users/zaranoia/Desktop/School/ET721_Fall_2024/lab7python_files/users.txt", "r")



print("\n --------------- Example 2: Python Limit to Read Files -------------")
print(fileusers.read(10))

print("\n --------------- Example 1: Python Files -------------")

# Use a relative or absolute path to users.txt

# for eachline in fileusers:
#     print(eachline)
    
print(fileusers.read())

fileusers.close()


print("\n --------------- Example 3: Python read files with 'with' and 'r' -------------")
with open("users.txt", "r") as fileusers:
    eachline = fileusers.read()
    print(eachline)