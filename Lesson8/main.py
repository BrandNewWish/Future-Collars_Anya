# def read_data(path):
#     with open(path) as fp:
#         return [line.strip() for line in fp if line and line[0] != '#']
#
from lesson8.FileCache import FileCache
from lesson8.FileReader import FileReader
from lesson8.Student import Student


# Opimized reading, because we load only necessary lines to RAM memory
def read_line(fp):
    while True:
        line = fp.readline()
        if line == "":
            return None
        if line and line[0] == '#':
            continue
        return line


# Yield works similar to the return but not breaks the function
def generator_1():
    yield 1


def generator_2():
    print("line 1")
    yield 1
    print("line 2")
    yield 2
    print("line 3")
    yield 3
    print("end")


# The best version of reading out files with comments (memory context)
def read_data(path):
    with open(path) as fp:
        for line in fp:
            if line and line[0] == "#":
                continue
            yield line.strip()


def main():
    fp = open("data.txt")
    # print(read_line(fp))

    for num in generator_2():
        print(num)

    for num in generator_1():
        print(num)

    print()

    for index, line in enumerate(read_data("data.txt")):
        print("{}) {}".format(index + 1, line))

    s1 = Student("John", "Doe", 5)
    s2 = Student("Jan", "Kowalski")
    print(s1.get_name())
    print(s2.get_name())
    print(s1)
    print(s2)
    print(int(s1))
    print(int(s2))

    if s1:
        print("{} is no longer in the first class".format(s1))

    print()

    fileCache = FileCache("data.json")
    fileCache.readchar(0)
    print(fileCache.cache)
    fileCache.readchar(1)
    print(fileCache.cache)
    fileCache.readchar(1)
    print(fileCache.cache)
    fileCache.readchar(2)
    print(fileCache.cache)
    fileCache.readchar(3)
    print(fileCache.cache)
    fileCache.readchar(4)
    print(fileCache.cache)

    for line in FileReader("data.json"):
        print(line)


main()