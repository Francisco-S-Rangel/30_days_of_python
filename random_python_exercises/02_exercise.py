def hello_world():
    print("Hello World")

def return_hello_world():
    return "Hello World"

hello_world()
print(return_hello_world())

def read_grade():
    return float(input("Type your grade: "))

def final_grade(grade_one, grade_two):
    final_grade = (grade_one + grade_two)/2
    print("Grade one: ", grade_one)
    print("Grande two: ", grade_two)
    print("Final score: ", final_grade, "Status: ", end="")
    if final_grade >= 6:
        print("Approved")
    else:
        print("Failed")

grade_one = read_grade()
grade_two = read_grade()
final_grade(grade_one,grade_two)

def return_final_grade(grade_one, grade_two):
    final_grade = (grade_one + grade_two)/2
    status = ""
    if final_grade >= 6:
        status = "Approved"
    else:
        status = "Failed"
    return f"Final score: {final_grade} , Status: {status}"

with open("./files/reading_final_grade.txt", "w") as file_final_grade:
    file_final_grade.write(return_final_grade(grade_one, grade_two))

reading_file = open("./files/reading_final_grade.txt")
print(reading_file.read())
reading_file.close()
