import json
import students
tasks = []


def main():
    while True:
        print("\n===TASK MANAGER===")
        print("1. Add a task")
        print("2.View a task")
        print("3. Delete a task")
        print("4. Mark a task done")
        print("5. Save tasks for later in a JSON file")
        print("0. Quit")
        tasks_number = len(tasks)
        choice = input("choose an option: ")
        if choice == "1":
            print("(Add a task here)")
            addTask()

        if choice == "4":
            t_num = int(input("What task have you completed?: ")) - 1
            markDone(tasks_number,t_num)

        if choice == "5":
            saveTasks(tasks_number)

        if choice == "3":
            t_num = int(input("What task number do you want to delete?: ")) - 1
            deleteTask(tasks_number,t_num)

        if choice == "0":
            print("Goodbye!")
            break

        if choice == "2":
            print("(View tasks here)")
            viewTask(tasks_number)


def addTask():
    task = input("Add task: ")
    status = "Complete" if (input("Have you completed the task? (y/n): ").lower()) == "y" else "Incomplete"
    new_task = {"name": task, "status": status}
    tasks.append(new_task)


def viewTask(t_no):
    hastask = checkForTask(t_no)
    if hastask:
        choice2 = int(input("Do you want to (1) View all tasks or (2) View specific task?"[0]))
        if choice2 == 2:
            t_toview = int(input("What task number would you specifically like to view?"))
            print(tasks[t_toview])
        else :
            print(tasks)


def deleteTask(t_no,t_num):
    hastask = checkForTask(t_no)
    if hastask:
        del tasks[t_num]


def markDone(t_no,t_num):
    hastask = checkForTask(t_no)
    if hastask:
        tasks[t_num]["status"] = "Completed"


def checkForTask(tasks_no):
    if tasks_no == 0:
        print("Task list is empty!")
        return False
    else:
        return True


def saveTasks(t_no):
    hastask = checkForTask(t_no)
    if hastask:
        confirm = input("Are you sure you want to save all tasks? (y/n): ")[0]
        if confirm.lower() == "y":
            with open("tasks.json", "w", encoding="utf-8") as outfile:
                json.dump(tasks, outfile, indent=4)
            print("Tasks saved to directory folder in \"tasks.json\"")

#We're making the users data set to be a nested dictionary that has Usernames as the initial key and the nested dictionary data set as it's assigned "value" pair


def auth_user(users):
   print("---Verification sign-in---")
   id = input("Enter registered student id: ")
   password = input("Enter password: ")
   if id in users:
       std_obj = users[id]
       pwd = std_obj.password
       if password == pwd:
           print("----Login successful, Welcome----")
           return True
       else:
           print("Incorrect password!")
           return False
   print("Username not found!")
   return False


if __name__ == "__main__":
    students.addStudent()
    registered_users = students.students
    if auth_user(registered_users):
        main()
    else:
        print("Access Denied!")
        raise ValueError("Incorrect username or password!!!")

