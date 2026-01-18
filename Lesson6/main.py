import csv
import json
import os
import sys
import pickle
import math
import random
import webbrowser

# =================================SYS===========================

print(sys.argv[0])  # Reserved for program name
# print(sys.argv[1]) #First need to provide arguments from terminal 'python.exe .\lesson6\main.py aaaaa bbbbb'
# print(sys.argv[2]) #First need to provide arguments from terminal 'python.exe .\lesson6\main.py aaaaa bbbbb'

sys.stdout.write("Message stdout\n")
sys.stderr.write("Message stderr\n")

# print("Enter value")
# value = sys.stdin.readline()
# print(value)


print(sys.platform)  # Operating system
print(sys.maxsize)  # 2^64-1 for 64bit, 2^32-1 for 32bit

# =================================OS==============================
# os.unlink("example.txt") #Removing file
print(os.getlogin())  # Logged user
print(os.getpid())  # Id of process
# print(os.get_terminal_size()) #Return terminal size (works only in terminal)
print(os.getcwd())  # Return current working directory
# os.mkdir("../lesson1/my_dir") #Creating directory
# os.remove("test.txt") #Remove file
# os.rename("my_dir", "my_dir_2") #Change name, works like cut and pase
# os.system("systeminfo") #Execute command like in CMD


print(os.path.exists(
    "C:\\Users\\Marek\\PycharmProjects\\futurecollars-marek-wisniewski\\FutureCollarsEN11"))  # Check if path exists (absolute)
print(os.path.exists("..\\..\\FutureCollarsEN11"))  # Check if path exists (relative)
print(os.path.isdir("my_dir_2"))  # Check if path is directory
print(os.path.isdir("test.txt"))  # Check if path is directory
print(os.path.basename(
    "C:\\Users\\Marek\\PycharmProjects\\futurecollars-marek-wisniewski\\FutureCollarsEN11\\lesson"))  # Returns parent directory
print(os.path.abspath("my_dir_2"))  # Returns absolute path based on relative path
print(os.path.abspath("..\\..\\..\\"))  # Returns absolute path based on relative path

# ============================JSON================================
person = {
    "name": "Marek",
    "age": 18,
    "is_programmer": True,
    "skills": ["Python", "JavaScript", "Java"]
}

json_string = json.dumps(person)  # SERIALIZATION - changing python object to json string
print(json_string)

fd = open("file.json", "w")
fd.write(json_string)
fd.close()

person_from_json = json.loads(json_string)  # DESERIALIZATION - convert json string to python object
print(person_from_json)

# ============================PICKLE==============================
# Supports sets and tuples
pickle_string = pickle.dumps(person)
print(pickle_string)

print(pickle.loads(pickle_string))

# ============================CSV=================================
with open("my_csv_file.csv", "w", newline="") as f:  # Save to csv
    writer = csv.writer(f, delimiter=';')  # ';' is default separator in excel
    writer.writerow([1, 2, 3, 4])
    writer.writerow(["aaaa", "bbbb", "cccc", "dddd"])
    writer.writerow(["Kraków", "Warszawa", "Wrocław", "Łódź"])

with open("my_csv_file.csv", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    for line in reader:
        print("|".join(line))

# ==========================Math================================
print(math.floor(3.9))  # Rounds down
print(math.ceil(3.5))  # Rounds up
print(math.fabs(-5))  # Returns absolute value
print(math.log(5))  # Logarithm
print(math.sin(45))  # Sine of number (in radians)
print(math.cos(45))  # Cosine of number (in radians)
print(math.fsum([1, 2, 3]))  # Sum of all elements

# =========================Random===============================
print(random.random())  # Returns a number from te 0-1 range
print(random.randrange(10, 1000, step=10))  # Returns random number from custom range
print(random.choice(["a", "b", "c"]))  # Returns random element from list

lst = ["a", "b", "c", "d", "e"]
random.shuffle(lst)  # Mixing order
print(lst)

print(random.sample(lst, k=3))

#====================Other useful packages =================
webbrowser.open('https://google.com')

date_now = datetime.now()
print(date_now)
print(date_now.year)
print(date_now.month)
print(date_now.day)

custom_date = date(2025, 1, 1)
print(custom_date)

# https://regex101.com/
text = "12345"
match = re.match("^\d\d\d\d$", text)
if match:
    print("Match")
else:
    print("Not match")