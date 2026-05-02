# 🍃 Cozy Todo List App

A beautiful and functional **GUI-based Todo List application** built with Python and CustomTkinter, developed as part of the **CodSoft Python Programming Internship** (Task 1).

---

## ✨ Features

- ➕ **Add Tasks** — with name, description, deadline, priority, category, and status
- 📋 **View All Tasks** — see every task in a clean scrollable card layout
- ⏳ **Pending Tasks** — filter and view only incomplete tasks
- 📊 **Dashboard** — highlights tasks due within 2 days or overdue
- ✏️ **Edit Tasks** — update any task detail on the fly
- 🗑️ **Delete Tasks** — remove tasks with auto ID reassignment
- ✔️ **Toggle Status** — mark tasks as Completed / Pending instantly
- 🔍 **Search Tasks** — find tasks by name in real time
- ⚠️ **Deadline Warnings** — auto flags tasks as `Overdue` or `Near Deadline`
- 💾 **Persistent Storage** — all tasks saved to `tasks.json` locally
- 📅 **Calendar Date Picker** — powered by `tkcalendar`

---

## 📸 Preview

> Run the app locally to see the full UI!

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| CustomTkinter | Modern dark-themed GUI |
| tkcalendar | Date picker widget |
| JSON | Local task storage |
| datetime | Deadline tracking & sorting |

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install customtkinter tkcalendar
```

### Run the App
```bash
python todogui.py
```
python todogui.py

> A `tasks.json` file will be created automatically in the same folder on first use.

---

## 📁 Project Structure

```
CODSOFT/
└── Task1-TodoList/
    ├── todogui.py
    └── tasks.json
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

## 💡 How It Works

1. **Dashboard** loads on startup — shows only urgent/overdue tasks
2. **Add** a task using the `+` floating button
3. **Edit or Delete** any task using the card action buttons
4. **Toggle** completion with the ✔ button on each card
5. **Search** for any task using the search button in the top bar
6. Tasks are **auto-sorted by deadline** and saved after every action

---

## ⚠️ Known Limitations

- No recurring tasks support
- Single user only (no multi-profile support)
- Tasks stored locally — no cloud sync

---

## 🔮 Future Improvements

- [ ] Wrap UI into a class-based structure
- [ ] Add reminder/notification support
- [ ] Filter by priority or category
- [ ] Export tasks to CSV or PDF
- [ ] Add dark/light theme toggle

---

## 👩‍💻 Author

Built with 🍃 as part of the **CodSoft Python Programming Internship**

---

## 📌 Tags

`#codsoft` `#internship` `#python` `#gui` `#customtkinter` `#todoapp` `#tkcalendar`
