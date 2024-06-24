import student

def load_students(file_name):
    list_of_students = []
    student1 = student.Student("Baljeet", "Patel", "Programming", 45, 4.14, 656565 )
    student2 = student.Student("Po", "The Dragon Warrior","Programming", 42, 4.78, 261715 )
    list_of_students.append(student1)
    list_of_students.append(student2)
    student_file = open(file_name, "r")
    student_file.readline()
    counter = 1
    for line_of_data in student_file:
        student_data = line_of_data.split(",")
        counter += 1
        try:
            studentx = student.Student(student_data[0], student_data[1], student_data[2], student_data[3], student_data[4], student_data[5])
            list_of_students.append(studentx)
        except:
            print(f"The students information is not loaded correctly at line {counter}")
    return list_of_students


def main():
    array = load_students("students.csv")
    for student in array:
            student.print_info()

main()
