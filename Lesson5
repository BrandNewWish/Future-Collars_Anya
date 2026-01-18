# import {local file name} import whole file
# from {local file name} import {class, function, variable} import specified thing

# from helper import TPL_FORMAT
# from helper import print_hello
# from helper import Point

# from helper import * import all - not recommended

from Lesson5.helper2 import print_hello as print_formal_hello
from Lesson5.helper import TPL_FORMAT, print_hello, Point

print(TPL_FORMAT.format("Marek"))

print_hello("Jan")
print_formal_hello("Jan")

p1 = Point(3, 4)
p2 = Point(5, 12)

print(p1.length())
print(p2.length())

print()
print()

# =========================Reading text file================================
fd = open("text.txt")
# print(fd.read()) #Read entire file, returns content as string
# print(fd.read(8)) #Read entire file, return content based on size (BYTES!)
# print(fd.readline()) #Read a single line
# print(fd.readline(8)) #Read a single line, return content based on size (BYTES!)
# print(fd.readlines()) #Read entire file, return content as list of strings
# print(fd.readlines(8)) #Read entire file, return content as list of strings, based on size (BYTES!)
fd.close()

# Read by lines in loop
fd = open("text.txt")
for line in fd:
    print(line)

fd.close()

# Reading with automatic close
with open("text.txt") as fd:
    for line in fd:
        print(line)
print("File is already closed")

# Writing to file
fd = open("text2.txt", "w")  # W - overwrite the file
fd.write("My Content \n")
fd.close()

fd = open("text2.txt", "a")  # A - append to file
fd.write("Line2 \n")
fd.write("Line3 \n")
fd.write("Line4 \n")
fd.close()

my_list = ["Line1 \n", "Line2 \n", "Line3 \n", "Line4\n"]

fd = open("text3.txt", "w")
fd.writelines(my_list)
fd.close()

print()
print()
# ==================Excercise=======================
counter = 0

with open("names.txt") as fd:
    for line in fd.readlines():
        print("Line{}: {}".format(counter, line[:-1]))
        counter += 1
