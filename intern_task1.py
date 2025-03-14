import tkinter as tk
from tkinter import messagebox
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = task_entry.get()
    if task:
        tasks = load_tasks()
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    tasks = load_tasks()
    for task in tasks:
        status = "✔" if task["completed"] else "✖"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

def mark_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks = load_tasks()
        tasks[selected_index]["completed"] = True
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks = load_tasks()
        tasks.pop(selected_index)
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=10)
add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

complete_button = tk.Button(button_frame, text="Mark Completed", command=mark_completed)
complete_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

update_listbox()

root.mainloop()
