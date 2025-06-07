import tkinter as tk
from tkinter import ttk
import string
import random

def generate_pass(length, alphabets, numbers, symbols):
    try:
        characters = ""

        if alphabets:
            characters += string.ascii_letters
        if numbers:
            characters += string.digits
        if symbols:
            characters += '@_!'

        if not characters:
            return "Select at least one character type!"

        return ''.join(random.choice(characters) for _ in range(int(length)))
    except ValueError:
        return "Invalid length!"

# ------------------ Main Window ------------------ #
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x550")
root.resizable(False, False)
bg_color = "#654702"
fg_color = "white"
root.configure(bg=bg_color)

# ------------------ Styles ------------------ #
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background=bg_color, foreground=fg_color, font=("Helvetica", 11))
style.configure("TButton", background="#a97404", foreground="white", font=("Helvetica", 11), padding=6)
style.configure("TCombobox",
    foreground="black",
    background="white",
    fieldbackground="#f5e7c0",
    selectbackground="#a97404",
    selectforeground="black",
    padding=5,
    font=("Helvetica", 11)
)
style.map("TCombobox",
    fieldbackground=[("readonly", "#f5e7c0")],
    background=[("readonly", "#f5e7c0")],
    foreground=[("readonly", "black")]
)

ttk.Label(root, text="Select length of password (4 to 16):").pack(pady=(20, 5))
options = list(range(4, 17))
length = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=length, values=options, state="readonly", width=10)
dropdown.pack(pady=5)
dropdown.current(0)

checkbox_style = {"bg": "#a97404", "fg": fg_color, "selectcolor": bg_color, "font": ("Helvetica", 12)}

def create_checkbox_box(text, variable):
    frame = tk.Frame(root, bg="#a97404", bd=2, relief="groove")
    frame.pack(pady=5, ipadx=10, ipady=5)
    cb = tk.Checkbutton(frame, text=text, variable=variable, **checkbox_style, width=25, anchor='w', padx=10)
    cb.pack()
    return frame

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

create_checkbox_box("Include Alphabets", var1)
create_checkbox_box("Include Numbers", var2)
create_checkbox_box("Include Symbols (@ _ !)", var3)

# ------------------ Result Label ------------------ #
result_entry = tk.Entry(root, font=("Courier New", 12, "bold"), justify="center", readonlybackground="#a97404", fg="white", width=30, border=1.5)
result_entry.pack(pady=20)
result_entry.configure(state='readonly')

# ------------------ Button ------------------ #
def handle_generate():
    pwd = generate_pass(length.get(), var1.get(), var2.get(), var3.get())
    result_entry.configure(state='normal')
    result_entry.delete(0, tk.END)
    result_entry.insert(0, pwd)
    result_entry.configure(state='readonly')

ttk.Button(root, text="Generate Password", command=handle_generate).pack(pady=10)

root.mainloop()