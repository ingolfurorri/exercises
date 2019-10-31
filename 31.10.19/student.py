class Student:
    def __init__(self, id, grades):
        self.__id = id
        self.__grades = grades

    def __lt__(self, obj):
        grade1 = 0
        grade2 = 0
        for grade in self.__grades:
            grade1 += grade
        grade1 /= len(self.__grades)

        for grade in obj.__grades:
            grade2 += grade
        grade2 /= len(obj.__grades)

        return grade1 < grade2

    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(self.__id, self.__grades)


a = Student(1, [3.0, 4.6, 3.4, 5.4])
b = Student(2, [9.5, 9.0, 8.9, 9.8])

print(a < b)