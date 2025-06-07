#FUNCTIONALITIES TO ADD
#Access from the terminal

import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkfont
import json
import os

DATA_FILE = "to_do_list/to_do_data.json"

# ------------------ Task Persistence ------------------ #
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# ------------------ Task Actions ------------------ #
def add_task():
    task_text = entry.get()
    if not task_text.strip():
        messagebox.showwarning("Input Error", "Please enter a task.")
        return
    tasks.append({"title": task_text.strip(), "completed": False})
    entry.delete(0, tk.END)
    update_task_list()
    save_tasks()

def toggle_complete(index):
    tasks[index]["completed"] = not tasks[index]["completed"]
    update_task_list()
    save_tasks()

def delete_task(index):
    del tasks[index]
    update_task_list()
    save_tasks()

# ------------------ GUI Rendering ------------------ #
def update_task_list():
    for widget in task_frame.winfo_children():
        widget.destroy()
    for i, task in enumerate(tasks):
        frame = ttk.Frame(task_frame, style="Task.TFrame")
        frame.pack(fill='x', pady=5, padx=5)

        var = tk.BooleanVar(value=task["completed"])
        style_name = "Done.TCheckbutton" if task["completed"] else "Task.TCheckbutton"
        cb = ttk.Checkbutton(frame, text=task["title"], variable=var,
                             command=lambda i=i: toggle_complete(i), style=style_name)
        cb.pack(side='left', fill='x', expand=True)

        del_btn = ttk.Button(frame, text="🗑", command=lambda i=i: delete_task(i), style="Delete.TButton")
        del_btn.pack(side='right', padx=5, pady=3)

# ------------------ Main Window ------------------ #
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="#1e1b2f")

# ------------------ Styles ------------------ #
style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background="#1e1b2f")
style.configure("TLabel", background="#1e1b2f", foreground="#f0e7ff", font=("Segoe UI", 12))
style.configure("Task.TFrame", background="#2a2540")
style.configure("TEntry", fieldbackground="#2a2540", foreground="#f0e7ff", borderwidth=1, relief="flat")
style.configure("TButton", background="#4c3575", foreground="#ffffff", font=("Segoe UI", 11), padding=6, relief="flat")
style.map("TButton",
          background=[("active", "#6541a5")],
          relief=[("pressed", "sunken")])
style.configure("Delete.TButton", background="#94475b", foreground="#fff")
style.configure("Delete.TButton", width=2.5, font=("Segoe UI Emoji", 12), relief="flat")
style.map("Delete.TButton", background=[("active", "#b04c6f")])

strike_font = tkfont.Font(family="Segoe UI", size=12, slant="italic", overstrike=1)
style.configure("Task.TCheckbutton", font=("Segoe UI", 12))
style.configure("Done.TCheckbutton", font=strike_font)

style.map("Task.TCheckbutton",
    background=[("active", "#3a3360"), ("!active", "#2a2540")],
    foreground=[("active", "#e0d9ff"), ("!active", "#f0e7ff")]
)
style.map("Done.TCheckbutton",
    background=[("active", "#3a3360"), ("!active", "#6f6691")],
    foreground=[("active", "#e0d9ff"), ("!active", "#f0e7ff")]
)

# ------------------ Widgets ------------------ #

entry = ttk.Entry(root, font=("Segoe UI", 13))
entry.pack(padx=15, pady=(20, 10), fill='x')
entry.bind("<Return>", lambda event: add_task())

add_btn = ttk.Button(root, text="Add Task", command=add_task, style="TButton")
add_btn.pack(pady=5)

# Scrollable task frame setup
container = ttk.Frame(root)
container.pack(fill='both', expand=True, padx=10, pady=10)

canvas = tk.Canvas(container, bg="#1e1b2f", highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

task_frame = ttk.Frame(canvas, style="TFrame")
task_frame_id = canvas.create_window((0, 0), window=task_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

task_frame.bind("<Configure>", on_frame_configure)

def resize_task_frame(event):
    canvas.itemconfig(task_frame_id, width=event.width)

canvas.bind("<Configure>", resize_task_frame)

# Mousewheel scroll
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

# ------------------ Init ------------------ #
tasks = load_tasks()
update_task_list()

root.mainloop()
