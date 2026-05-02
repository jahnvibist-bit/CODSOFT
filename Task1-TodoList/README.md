# 🍃 Cozy Todo List App

> Started as a simple terminal app — then upgraded to a full GUI! 💻✨

This project shows my progression from a **command-line Todo app** to a fully featured **GUI application** built with CustomTkinter — same logic, better experience!

---

## 📁 Versions

| Version | File | Type |
|---------|------|------|
| 🖥️ Terminal | `todo_terminal.py` | Command Line |
| 🎨 GUI | `todogui.py` | CustomTkinter |

---

## 🖥️ Terminal Version

### ✨ Features
- ➕ **Add Tasks** — name, description, deadline, priority, category, status
- 🗑️ **Delete Tasks** — confirmation prompt + auto ID reassignment
- ✏️ **Update Tasks** — update specific fields individually
- 📋 **View All Tasks** — formatted table view
- 🔍 **Search Tasks** — find task by name
- ⏳ **Pending Tasks** — filter incomplete tasks only
- 📊 **Task Stats** — total, completed and pending count
- 📅 **Sort by Deadline** — auto sorts tasks by due date
- ⚠️ **Deadline Warnings** — alerts on startup for overdue tasks
- 💾 **Persistent Storage** — saved to `tasks.json`

### 🚀 Run Terminal Version

```bash
python todo_terminal.py
```

### 💡 How It Works

```
Startup → load tasks.json → check deadlines → show menu
```

Number-based menu (1-9) for all operations. Validates all inputs before saving!

---

## 🎨 GUI Version

### ✨ Features
- ➕ **Add Tasks** — via popup window with calendar date picker
- 📋 **View All Tasks** — scrollable card layout
- ⏳ **Pending Tasks** — filter view for incomplete tasks
- 📊 **Dashboard** — shows only urgent/overdue tasks
- ✏️ **Edit Tasks** — update any detail on the fly
- 🗑️ **Delete Tasks** — with auto ID reassignment
- ✔️ **Toggle Status** — mark Completed / Pending instantly
- 🔍 **Search Tasks** — real time search by name
- ⚠️ **Deadline Warnings** — auto flags `Overdue` or `Near Deadline`
- 💾 **Persistent Storage** — saved to `tasks.json`
- 📅 **Calendar Date Picker** — powered by `tkcalendar`

### 🚀 Run GUI Version

```bash
pip install customtkinter tkcalendar
python todogui.py
```

---

## 🔮 Why I Upgraded to GUI

After building the terminal version I realised:
- Terminal apps are hard for non-technical users
- Deadline tracking needed a **visual dashboard**
- Cards and scrollable views make tasks easier to manage
- A floating `+` button is way more fun than typing `1` 😄

So I rebuilt it as a full GUI app — same core logic, completely new experience!

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| CustomTkinter | GUI framework |
| tkcalendar | Date picker widget |
| JSON | Local task storage |
| datetime | Deadline tracking |
| match/case | Terminal menu navigation |

---

## 📁 Project Structure

```
CODSOFT/
└── Task1-TodoList/
    ├── todo_terminal.py     
    ├── todogui.py           
    ├── tasks.json           
    └── README.md            
```

---

## 🗂️ Task Fields

| Field | Description |
|-------|-------------|
| `id` | Auto-assigned unique ID |
| `name` | Task title |
| `description` | Short description |
| `deadline` | Due date (DD-MM-YYYY) |
| `priority` | High / Medium / Low |
| `category` | User-defined category |
| `status` | Pending / Completed |
| `created_date` | Date task was added |
| `warning` | Overdue / Near Deadline / "" |

---

## 👩‍💻 Author

Built with 🍃 as part of the **CodSoft Python Programming Internship**

---

## 📌 Tags

`#codsoft` `#internship` `#python` `#gui` `#terminal` `#customtkinter` `#todoapp` `#tkcalendar`ogramming Internship**

---

## 📌 Tags

`#codsoft` `#internship` `#python` `#gui` `#customtkinter` `#todoapp` `#tkcalendar`
