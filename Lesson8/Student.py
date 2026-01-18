class Student:
    def __init__(self, firstname, lastname, year=1, group="A"):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.group = group

    def get_name(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __int__(self):
        return self.year

    def __float__(self):
        return self.year

    def __bool__(self):
        return self.year > 1