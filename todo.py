from guizero import App, Text, TextBox, PushButton, ListBox, Box, info, yesno
from time import time, ctime

tasks = []

# Function to add a new task
def add_task():
    task_name = task_name_input.value
    if task_name:
        task_info = {"name": task_name, "timestamp": ctime(time())}
        tasks.append(task_info)
        update_task_list()
        task_name_input.value = ""


# Function to update the selected task
def update_task():
    selected_task = task_listbox.value
    new_task_name = task_name_input.value
    if selected_task and new_task_name:
        index = task_listbox.items.index(selected_task)
        tasks[index]["name"] = new_task_name
        tasks[index]["timestamp"] = ctime(time())  # Update the timestamp
        update_task_list()
        task_name_input.value = ""



# Function to remove the selected task
def remove_task():
    selected_task = task_listbox.value
    if selected_task:
        if yesno("Confirm", f"Are you sure you want to remove the task '{selected_task}'?"):
            index = task_listbox.items.index(selected_task)
            tasks.pop(index)
            update_task_list()

# Function to track and display the selected task's details
def track_task():
    selected_task = task_listbox.value
    if selected_task:
        index = task_listbox.items.index(selected_task)
        task = tasks[index]
        info("Task Details", f"Task: {task['name']}\nAdded/Updated at: {task['timestamp']}")

# Function to update the task list displayed in the ListBox
def update_task_list():
    task_listbox.clear()
    for task in tasks:
        task_listbox.append(task['name'])

# Initialize the GUI
app = App("To-Do List", width=400, height=400)

# Box to hold input fields
input_box = Box(app, layout="grid")
Text(input_box, text="Task Name:", grid=[0, 0])
task_name_input = TextBox(input_box, grid=[1, 0])

# Buttons for task actions
btn_box = Box(app, layout="grid")
PushButton(btn_box, text="Add Task", command=add_task, grid=[0, 0])
PushButton(btn_box, text="Update Task", command=update_task, grid=[1, 0])
PushButton(btn_box, text="Remove Task", command=remove_task, grid=[2, 0])
PushButton(btn_box, text="Track Task", command=track_task, grid=[3, 0])

# ListBox to display tasks
task_listbox = ListBox(app, items=[], width="fill", height="fill", scrollbar=True)

# Display the GUI
app.display()

