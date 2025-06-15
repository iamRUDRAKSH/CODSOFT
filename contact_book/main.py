import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import re

DATA_FILE = "contact_book/contact_list.json"

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts():
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_phone(phone):
    return phone.isdigit() and len(phone) >= 7

def add_contact():
    Name = entry1.get()
    Phone = entry2.get()
    Email = entry3.get()
    Address = entry4.get()

    if Name == "Name" or Phone == "Phone number" or Email == "Email" or Address == "Address":
        messagebox.showwarning("Input Error", "Please fill all the fields")
        return

    if not (Name.strip() and Phone.strip() and Email.strip() and Address.strip()):
        messagebox.showwarning("Input Error", "Please fill all the fields")
        return
    if not validate_phone(Phone):
        messagebox.showerror("Invalid Input", "Phone number should contain only digits and be at least 7 digits long.")
        return
    if not validate_email(Email):
        messagebox.showerror("Invalid Input", "Please enter a valid email address.")
        return

    contacts.append({
        "store_name": Name.strip(),
        "phone_number": Phone.strip(),
        "email": Email.strip(),
        "address": Address.strip()
    })
    placeholders = ["Name", "Phone number", "Email", "Address"]
    for e, p in zip([entry1, entry2, entry3, entry4], placeholders):
        e.delete(0, tk.END)
        add_placeholder(e, p)

    update_contact_list()
    save_contacts()

def delete_contact(index):
    del contacts[index]
    update_contact_list()
    save_contacts()

def search_contact(event=None):
    keyword = search_entry.get().lower().strip()
    filtered = [c for c in contacts if (
        keyword in c["store_name"].lower() or
        keyword in c["phone_number"] or
        keyword in c["email"].lower() or
        keyword in c["address"].lower()
    )]
    update_contact_list(filtered)

def update_contact_list(filtered_contacts=None):
    tree.delete(*tree.get_children())
    for contact in filtered_contacts if filtered_contacts is not None else contacts:
        tree.insert("", "end", values=(
            contact["store_name"],
            contact["phone_number"],
            contact["email"],
            contact["address"],
            "🗑"
        ))

def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(foreground="gray")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(foreground=fg_color)

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(foreground="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def on_treeview_click(event):
    region = tree.identify("region", event.x, event.y)
    if region == "cell":
        col = tree.identify_column(event.x)
        row = tree.identify_row(event.y)
        if col == "#5":  # 5th column (Delete action)
            if row:
                index = tree.index(row)
                confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
                if confirm:
                    delete_contact(index)

# ------------------ GUI Setup ------------------ #
root = tk.Tk()
root.title("Contact Book")
root.geometry("800x600")
root.resizable(False, False)

# Theme colors
root_bg = "#005d25"
fg_color = "#e0f2e9"  # light mint-ish for good contrast

root.configure(bg=root_bg)

style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background=root_bg)
style.configure("TLabel", background=root_bg, foreground=fg_color, font=("Segoe UI", 12))
style.configure("TEntry",
                fieldbackground=root_bg,
                foreground=fg_color,
                borderwidth=1,
                relief="flat",
                insertcolor=fg_color)
style.configure("TButton",
                background="#4c7a4c",  # slightly lighter green
                foreground=fg_color,
                font=("Segoe UI", 11),
                padding=6,
                relief="flat")
style.map("TButton", background=[("active", "#6cbf6c")])

style.configure("Treeview",
                background=root_bg,
                fieldbackground=root_bg,
                foreground=fg_color,
                font=("Segoe UI", 11),
                rowheight=30,
                bordercolor=root_bg,
                borderwidth=0)
style.configure("Treeview.Heading",
                background="#3d7a3d",
                foreground=fg_color,
                font=("Segoe UI", 12, "bold"))

# ------------------ Entry Fields ------------------ #
search_entry = ttk.Entry(root, font=("Segoe UI", 13))
search_entry.pack(padx=15, pady=(20, 10), fill='x')
add_placeholder(search_entry, "Search by name...")
search_entry.bind("<Return>", search_contact)

entry1 = ttk.Entry(root, font=("Segoe UI", 12))
entry1.pack(padx=15, pady=(5, 0), fill='x')
add_placeholder(entry1, "Name")

entry2 = ttk.Entry(root, font=("Segoe UI", 12))
entry2.pack(padx=15, pady=(5, 0), fill='x')
add_placeholder(entry2, "Phone number")

entry3 = ttk.Entry(root, font=("Segoe UI", 12))
entry3.pack(padx=15, pady=(5, 0), fill='x')
add_placeholder(entry3, "Email")

entry4 = ttk.Entry(root, font=("Segoe UI", 12))
entry4.pack(padx=15, pady=(5, 0), fill='x')
add_placeholder(entry4, "Address")

add_btn = ttk.Button(root, text="Add Contact", command=add_contact, style="TButton")
add_btn.pack(pady=10)

# ------------------ Treeview Table ------------------ #
table_frame = ttk.Frame(root, style="TFrame")
table_frame.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("Name", "Phone", "Email", "Address", "Action")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", style="Treeview")

for col in columns:
    tree.heading(col, text=col)
    if col == "Action":
        tree.column(col, anchor="center", width=80)
    else:
        tree.column(col, anchor="w", width=150)

tree.pack(fill="both", expand=True, side="left")

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

tree.bind("<Button-1>", on_treeview_click)

# ------------------ Init ------------------ #
contacts = load_contacts()
update_contact_list()

root.protocol("WM_DELETE_WINDOW", lambda: (save_contacts(), root.destroy()))
root.mainloop()