# To-Do List Management Application
import json
file_path = "./Project-3/todo_list.json"

def load_tasks():
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return {"tasks":[]}

def save_tasks(tasks):
    try:
        with open(file_path, "w") as file:
            json.dump(tasks, file)
    except Exception as e:
        print(f"Error saving tasks: {e}")


def view_task(tasks):
    for index, task in enumerate(tasks["tasks"], start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index}. {task['title']} - {status}")

def add_task(tasks):
    title = input("Enter the title of the task: ").strip()
    description = input("Enter the description of the task: ").strip()
    tasks["tasks"].append({"title": title, "description": description, "completed": False})

def delete_task(tasks):
    view_task(tasks)
    task_index = int(input("Enter the index of the task to delete: "))
    tasks["tasks"].pop(task_index - 1)
    
def mark_task_as_completed(tasks):
    view_task(tasks)
    task_index = int(input("Enter the index of the task to mark as completed: "))
    tasks["tasks"][task_index - 1]["completed"] = True

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Management Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Save and Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_as_completed(tasks)
        elif choice == "5":
            print("Saving tasks...")
            save_tasks(tasks)
            print("Tasks saved successfully.")
            break
        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()