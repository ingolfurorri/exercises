def get_student_list():
    student_list = []
    for i in range(4):
        student = input("Enter student: ")
        grades = []
        for j in range(3):
            print("Enter grade number {}:".format(j+1), end=' ')
            grades.append(input())
        student_list.append([student, grades])

    return sorted(student_list)


def get_average(student_grade):
    average = 0
    for grade in student_grade:
        average += int(grade)

    return average / len(student_grade)




def get_highest_grade(student_list):
    highest_average = 0
    student_index = 0
    for index, student in enumerate(student_list):
        average = get_average(student[1])
        if(average > highest_average):
            highest_average = average
            student_index = index

    return highest_average, student_index



def print_list(student_list):
    for student in student_list:
        print("{}: {}".format(student[0], student[1]))
    
    print("Student with highest average grade: ")
    highest_average, student_index = get_highest_grade(student_list)
    print("{} has an average grade of {}".format(student_list[student_index][0], highest_average))



def main():
    student_list = get_student_list()
    print(student_list)
    print_list(student_list)


main()