def display_menu():
    print("View tasks")
    print("Create a new task")
    print("Delete a new task")
    print("Exit")

def add_task(tasks):
    task = input("\nPlease enter your tasks here: ")
    tasks.append(task)
    print("task was successfully entered")

add_task( "hello")