def display_menu():
    print("\n1.  View tasks")
    print("2. Create a new task")
    print("3. Delete a new task")
    print("4. Exit")

def view_task(tasks):
    if not tasks:
        print("\n No Tasks!")
    else:
        print("Your Tasks: ")
        for i, (tasks, completed) in enumerate (tasks, 1):
            status = "c" if completed else "N"
            print(f"{i}. {tasks} [{status}]")
    
def add_task(tasks):
    task = input("\n Enter your task")
    tasks.append((task, False))
    print("Tasked added sucessfully")



def delete_task(tasks):
   view_task(tasks)
   if tasks:
        '''Try { task} except {catching an error} is to catch certain error 
        and doing something specific to them'''
        try: 
            task_num =  int(input("\n Enter the task number to delete: "))
            tasks.pop(task_num - 1)
            print("Deletion was sucessful")
        except (ValueError, IndexError):
            print("Invalid number")


  
   
   
       

def main() :
    tasks = []
    while True:
        display_menu()
        choice = input("\n Enter your option: ")
        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3" :
            delete_task(tasks)
        elif choice == "4":
            print("Exit the application!")
            break
        else:
            print("Invalid entry, try again")

            

# Why assign the list function in a if statement?

if __name__ == "__main__" :
    main()
