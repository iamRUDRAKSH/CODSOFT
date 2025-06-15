# 📒 Contact Book - Tkinter GUI Application

A modern, interactive Contact Book made using Python's `tkinter` library.  
This app lets you **store**, **search**, and **delete** contacts easily — all within a clean graphical interface.

---

## ✨ Features

- 🔍 Search contacts by name, phone, email, or address
- ➕ Add new contacts with validation for phone numbers and email
- 🗑 Delete contacts with confirmation prompts
- 📁 Persistent storage using a local JSON file
- 🎨 Clean, dark-themed UI using the `clam` theme

---

## 📦 Requirements

- Python 3.x
- No external dependencies — uses only Python standard libraries

---

## 🛠 How to Run

1. Clone or download this repository.
2. Ensure you have Python installed.
3. Run the script:

```bash
python main.py
```

> Make sure the directory `contact_book/` exists with write permissions, or the app will create the `contact_list.json` file automatically in that directory.

---

## 📁 Project Structure

```
contact_book/
├── contact_list.json   # JSON file that stores the contacts
└── main.py     # Main application script
```

---

## 🧠 Validations

- **Phone number** must be digits only and at least 7 characters long.
- **Email** must be in a valid format (e.g., `user@example.com`).
- All fields are required for adding a contact.

---

## 💡 UI Overview

- Entry placeholders guide input (`Name`, `Phone number`, etc.).
- Press `Enter` in the search field to filter contacts.
- Click the 🗑 icon in the Action column to delete a contact.

---

## 🛡️ Data Safety

- Contact data is stored locally in a JSON file.
- Data is saved on every add/delete and upon closing the app.

---

## 📄 License

Free to use for educational and personal projects.

---

Made with ❤️ using Tkinter