tasks = [{"category": "school", "title": "homework", "done": False},
         {"category": "Home", "title": "cleaning", "done": False},
         {"category": "Work", "title": "project", "done": False},
         {"category": "Grocery", "title": "shopping", "done": False},
         {"category": "Exercise", "title": "gym", "done": False},
         {"category": "Hobby", "title": "painting", "done": False}]
         
while True:
    print("\n1. View tasks")
    print("2. Add task(s)")
    print("3. task status")
    print("4. Edit task(s)")
    print("5. Remove task")
    print("6. Exit")
    
    choice = input("Select option from menu: ")
    for idx, task in enumerate(tasks, start=1):
        status = "#" if task["done"] else "*"
    
    if choice == '1':
        if not tasks:
            print("No task availlable! Enter option 2 to add new task.")

        else:
            print("\nYour tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. [{status}] {task['category']}: {task['title']}")
                
    elif choice == '2':
        add_task_category = input("Enter task category: ")
        add_task_title = input("Enter task title: ")
        if add_task_category == "-1" and add_task_title == "-1":
            print("Task addition cancelled! Returning to menu...")

        else:
            tasks.append({"category": add_task_category, "title": add_task_title, "done": False})
            print("Task added successfully!")
            print("\nNew task list: ")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. [{status}] {task['category']}: {task['title']}")
                
    elif choice == '3':
        change_status = int(input("Enter task number to change status: "))
        if change_status == -1:
            print("Status change cancelled! Returning to menu...")

        else:
            if 1 <= change_status <= len(tasks):
                change_status = change_status - 1   
                status_mark = input("Enter status_sign: ")
                tasks[change_status]["done"] = status_mark
                print("Task marked successfully!")
                print("\nTask list after change: ")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. [{task['done']}] {task['category']}: {task['title']}")

            else:
                print("Invalid task number! Please try again and select a valid task number to change status.")        
            
    elif choice == '4':
        edit_task = int(input("Enter task number to edit: "))
        if edit_task == -1:
            print("Task editing cancelled! Returning to menu...")

        else:
            if 1 <= edit_task <= len(tasks):
                replacement = input("what do you want to edit? (category/title): ").lower()
                if replacement == "category":
                    new_value = input("Enter new category: ")
                    tasks[edit_task - 1]["category"] = new_value
                elif replacement == "title":
                    new_value = input("Enter new title: ")
                    tasks[edit_task - 1]["title"] = new_value
                    print(f"Task {edit_task} editted successfully!")
                    print("\nNew task list: ")
                    for idx, task in enumerate(tasks, start=1):
                        print(f"{idx}. [{status}] {task['category']}: {task['title']}")

            else:
                print("Invalid task number! Please try again.")

    elif choice == '5':
        removed_task = int(input("Enter task number to remove: "))
        if removed_task == -1:
            print("Task removal cancelled! Returning to menu...")

        else:
            if 1 <= removed_task <= len(tasks):
                tasks.pop(removed_task - 1)
                print(f"Task {removed_task} removed successfully!")
                print("\nNew task list: ")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. [{status}] {task['category']}: {task['title']}")

            else:
                print("Invalid task number! Please try again and select a valid task number to remove.")    
                
    elif choice == '6':
        exit = input("Are you sure you want to exit? (YES/NO): ").upper()
        if exit == "YES":
            print("Exiting the program...")
            break
        elif exit == "NO":
            print("Exit cancelled! Returning to menu...")
    else:
        print("Invalid input! Please try again.")