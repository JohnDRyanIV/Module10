class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        gpa_characters = set("1234567890.")
        '''Examples of provided majors the program will check against, real database would have many more'''
        majors = {"Aviation", "Comp Sci", "Engineering", "Political Science", "Anthropology", "Mathematics", "English"}
        if lname in majors or fname in majors or not name_characters.issuperset(lname):
            raise ValueError

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
