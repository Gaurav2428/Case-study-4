tasks = {}
def add_task():
task_id = str(len(tasks) + 1)
task_desc = f"[ ] Task {task_id}"
tasks[task_id] = {"description": task_desc, "completed": False}
print(f"{task_desc} added successfully!\n")
def view_tasks():
if not tasks:
print("No tasks.\n")
return
for task_id, task in tasks.items():
status = "✔ Completed" if task["completed"] else "❌ Pending"
print(f"{task_id}. {task['description']} - {status}")
print()
def delete_task():
view_tasks()
task_id = input("Enter task ID to delete: ")
if task_id in tasks:
status = "✔" if tasks[task_id]["completed"] else "❌"
del tasks[task_id]
print(f"Task {task_id} {status} deleted successfully!\n")
else:
print("Invalid Task ID.\n")
def mark_complete():
task_id = input("Enter task ID to mark complete: ")
if task_id in tasks:
tasks[task_id]["completed"] = True
tasks[task_id]["description"] = tasks[task_id]["description"].replace("[ ]", "[✔]")
print(f"Task {task_id} marked as completed!\n")
else:
print("Invalid Task ID.\n")
def main():
while True:
print("1. Add Task")
print("2. View Tasks")
print("3. Delete Task")
print("4. Mark Task Complete")
print("5. Exit")
choice = input("Enter your choice: ")
if choice == "1":
add_task()
elif choice == "2":
view_tasks()
elif choice == "3":
delete_task()
elif choice == "4":
mark_complete()
elif choice == "5":
print("Exiting To-Do Notes Builder. Goodbye!")
break
else:
print("Invalid choice! Please try again.\n")
if __name__ == "__main__":
main()
