import json
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
        choice = input("choose an option: ")
        if choice == "1":
            print("(Add a task here)")
            addTask()
            
        if choice == "4":
            t_num = int(input("What task have you completed?: ")) - 1 
            markDone(t_num)

        if choice == "5":
            saveTasks()


        if choice == "3":
            t_num = int(input("What task number do you want to delete?: ")) - 1
            deleteTask(t_num)

        if choice == "0":
            print("Goodbye!")
            break
            
        if choice == "2":
            print("(View tasks here)")
            viewTask()
            



def addTask():
    task = input("Add task: ")
    status = "Complete" if(input("Have you completed the task? (y/n): ").lower()) =="y" else "Incomplete"
    new_task = {"name": task, "status":status}
    tasks.append(new_task)
    


def viewTask():
    choice2 = int(input("Do you want to (1) View all tasks or (2) View a specific task: "))
    if  not tasks:
        print("Task list is empty!")

    else:
        if choice2 == 2:
            t_num = int(input("What task number do you want to view?: "))
            print(tasks[t_num-1])

        else:
            print(tasks)


def deleteTask(t_num):
    del  tasks[t_num]

def markDone(t_num):
    tasks[t_num]["status"] = "Completed"

def saveTasks() :
    confirm = input("Are you sure you want to save all tasks? (y/n): ")
    if confirm.lower()== "y" or confirm.lower()== "yes":
        with open("tasks.json", "w", encoding = "utf-8") as outfile:
            json.dump(tasks, outfile, indent =4)
        print("Tasks saved to directory folder in \"tasks.json\"")



main()            