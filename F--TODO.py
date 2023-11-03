import tkinter as tk

tasks = []

def show_menu():
    print("Menu:")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Quit")

def add_task(task):
    tasks.append({"task": task, "done": False})
    print("Task added!")

def list_tasks():
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['task']} - {status}")

def mark_task_done(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task index.")

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed task: {removed_task['task']}")
    else:
        print("Invalid task index.")

def add_task_tk():
    task = entry.get()
    if task:
        add_task(task)
        update_task_listbox()
        entry.delete(0, tk.END)

def remove_task_tk():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        remove_task(task_index + 1)  # Adding 1 since tkinter indexing starts at 0
        update_task_listbox()

def mark_task_done_tk():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        mark_task_done(task_index + 1)  # Adding 1 since tkinter indexing starts at 0
        update_task_listbox()
        print("Task marked as done!")

def update_task_listbox():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Done" if task["done"] else "Not Done"
        tasks_listbox.insert(tk.END, f"{task['task']} - {status}")

def add_user_input():
    year = year_entry.get()
    month = month_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    task = entry.get()
    if year and month and date and time and task:
        task_with_datetime = f"{year}-{month}-{date} {time}: {task}"
        add_task(task_with_datetime)
        update_task_listbox()
        entry.delete(0, tk.END)
        year_entry.delete(0, tk.END)
        month_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)

app = tk.Tk()
app.title("To-Do List")
app.configure(bg='black')

entry = tk.Entry(app, width=40, bg='white', fg='black')
entry.pack(pady=10)

year_label = tk.Label(app, text="Year:", bg='black', fg='white')
year_label.pack()
year_entry = tk.Entry(app, width=10, bg='white', fg='black')
year_entry.pack()

month_label = tk.Label(app, text="Month:", bg='black', fg='white')
month_label.pack()
month_entry = tk.Entry(app, width=10, bg='white', fg='black')
month_entry.pack()

date_label = tk.Label(app, text="Date:", bg='black', fg='white')
date_label.pack()
date_entry = tk.Entry(app, width=10, bg='white', fg='black')
date_entry.pack()

time_label = tk.Label(app, text="Time (HH:MM):", bg='black', fg='white')
time_label.pack()
time_entry = tk.Entry(app, width=10, bg='white', fg='black')
time_entry.pack()

add_button = tk.Button(app, text="Add Task", command=add_user_input, bg='white', fg='black')
add_button.pack()

tasks_listbox = tk.Listbox(app, width=40, bg='black', fg='white')
tasks_listbox.pack()

remove_button = tk.Button(app, text="Remove Task", command=remove_task_tk, bg='white', fg='black')
remove_button.pack()

mark_done_button = tk.Button(app, text="Mark Task Done", command=mark_task_done_tk, bg='white', fg='black')
mark_done_button.pack()

app.mainloop()
