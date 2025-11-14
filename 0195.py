# 3. To-Do list Manager
todo_list = []
while True:
    print("\n=== To-Do List ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    
    choice = input("Choose option (1-4): ")
    
    if choice == '1':
        task = input("Enter task: ")
        todo_list.append(task)
        print(f"Task '{task}' added successfully!")
        
    elif choice == '2':
        if todo_list:
            print("Your tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks in list!")
            
    elif choice == '3':
        if todo_list:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number!")
                
        else:
            print("No tasks to remove!")
            
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-4.")