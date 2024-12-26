def display_menu():
    print("1. View tasks")
    print("2. Create a new task")
    print("3. Delete a new task")
    print("4. Exit")

def add_task(tasks):
    task = input("\n Enter your task")
    tasks.append(task, False)
    print("Tasked added sucessfully")

def view_task():
    current = add_task()
    print(current)

def delete_task(tasks):
   task = tasks.remove()
   print(task)

def main() :
    tasks = []
    while True:
        display_menu()
        choice = input("\n Enter your choice")

        if choice == 1 :
            view_task()
        elif choice == 2 :
            add_task()
        elif choice == 3 :
            delete_task()
        elif choice == 4:
            print("Exit the application!")
            

# Why assign the list function in a if statement?

if __name__ == "__main__" :
    main()
