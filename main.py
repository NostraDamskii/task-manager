from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "add":
            new_task=input("Enter yor task")
            try:
                manager.add_task(new_task)
            except ValueError:
                print("Empty task")
            except TypeError:
                print("Wrong type")
        elif command == "list":
            for i,task in enumerate(manager.list_tasks()):
                print(f"{i}. {task}")
        elif command == "done":
            task_index=input("Which task did you complete? Type index")
            try:
                manager.mark_task_done(int(task_index))
                print(f"Task done")
            except IndexError:
                print("Wrong index!")
            except ValueError:
                print("Index should be an integer ")
        elif command == "remove":
            task_index=input("Which task do you want to remove? Type index")
            try:
                manager.remove_task(int(task_index))
                print(f"Task removed")
            except IndexError:
                print("Wrong index!")
            except ValueError:
                print("Index should be an integer ")
        elif command == "exit":
            print("Program end")
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
