import json
import os
import datetime
checklist = []

DATA_FILE = "checklist_manager.json"
def load_checklist():
  if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as json_file:
            loaded_dict = json.load(json_file)
            print(loaded_dict)
            return loaded_dict
    return []
  
def add_task(checklist):
  new_task = input ('Add a task:')
  print("Please enter task details: description,due_date, priority, assigned person and notes" )

description = input("Enter task description: ")
due_date = input("Enter due date (YYYY-MM-DD): ")
priority = input("Enter priority level (High, Medium, Low): ")
assigned_person = input("Enter assigned person/team: ")
notes = input("Enter any additional notes: ")

# Create a task dictionary
task = {
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "assigned_person": assigned_person,
        "notes": notes,
        "completed": False
    }
checklist.append({"task": task, "completed": False})
for task in checklist:
  print("Task added!")


def view_task(checklist):
  for index, task_item in enumerate(checklist):
    print(f"{index + 1}. {task_item['task']} (Completed: {task_item['completed']})")


def edit_task():
    view_task()
    task_num = int(input("Enter the task number to edit: ")) - 1

    if 0 <= task_num < len(checklist):
        task = checklist[task_num]
        task["description"] = input(f"New description (current: {task['description']}): ") or task["description"]
        task["due_date"] = input(f"New due date (current: {task['due_date']}): ") or task["due_date"]
        task["priority"] = input(f"New priority (current: {task['priority']}): ") or task["priority"]
        task["assigned_person"] = input(f"New assigned person (current: {task['assigned_person']}): ") or task["assigned_person"]
        task["status"] = input(f"New status (current: {task['status']}): ") or task["status"]
        print("Task updated successfully!\n")
    else:
        print("Invalid task number.\n")

# Delete a task
def delete_task(checklist):
    task_num = int(input("Enter the task number to delete: ")) - 1

    if 0 <= task_num < len(checklist):
        task = checklist.pop(task_num)
        print(f"Task '{task['description']}' deleted successfully!\n")
    else:
        print("Invalid task number.\n")

def save_task(checklist, filename="checklist.json"):
  with open(filename, "w") as f:
    json.dump(checklist, f)
  print("checklist saved!")

# Check for upcoming due dates
def reminders_for_due_dates(checklist):  
    reminder_days = int(input("Enter the number of days for reminder: "))
    today = datetime.date.today()
    upcoming_tasks = [task for task in checklist if task["task"]["due_date"]]
    print("\nUpcoming Due Dates:")
    for task in upcoming_tasks:
        due_date = datetime.datetime.strptime(task["task"]["due_date"], "%Y-%m-%d").date()
        if today <= due_date <= today + datetime.timedelta(days=reminder_days):
            print(f"Task '{task['description']}' is due on {due_date}.\n")

def update_task_status(checklist):
    view_task(checklist) 
    task_num = int(input("Enter the task number to update status: ")) - 1

    if 0 <= task_num < len(checklist):
        task = checklist[task_num]
        task["status"] = input("Enter new status (Not Started, In Progress, Completed, On Hold): ")
        task["completed"] = True if task["status"].lower() == "completed" else False
        print("Task status updated successfully!\n")
    else:
        print("Invalid task number.\n")

def main(checklist):
   # Load the checklist from the file when the program starts
  checklist = load_checklist() 
  while True:
        print("\n--- Product Launch Checklist Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Reminders for Upcoming Due Dates")
        print("7. Update Task Status")
        print("8. Exit")

choice = input("Enter your choice: ")

if choice == '1':
            add_task(checklist)
elif choice == '2':
            view_task(checklist)
elif choice == '3':
            edit_task(checklist)
elif choice == '4':
            delete_task(checklist)
elif choice == '5':
            save_task(checklist)
elif choice == '6':
            reminders_for_due_dates(checklist)
elif choice == '7':
            update_task_status(checklist)
elif choice == '8':
            print("Exiting the Checklist Manager. Goodbye!")
else:
            print("Invalid choice. Please try again.\n")


