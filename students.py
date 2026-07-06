class Student:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        #self.grades = grades


students = {}


def addStudent():
    while True:
        id = input("Enter student id (\"quit\" to quit): ").strip()
        if id.lower() == "quit":
            break
        name = input("Enter student username: ").strip()
        password = input("Enter student password: ")
        """ grades_input = input("Enter grades separated by \",\": ").strip().split(",")
        grades = [int(g.strip()) for g in grades_input if g.strip().isdigit() and int(g.strip()) <= 100]"""
        student = Student(name, password)
        students[id] = student
        print(student.grades)

if __name__ == "__main__":
    addStudent()
    print(students)




