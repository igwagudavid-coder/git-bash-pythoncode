students = []
while True:
    std_name = input("Enter Student name: ")
    std_id = input("Enter student ID: ")
    std_age = input("Enter your age: ")
    std_data = {"name":std_name, "id":std_id , "age": std_age}

    students.append(std_data)
    choice = input("Do you want to end?: ")
    if choice =="yes":
        break
print(students[0].get("id"))