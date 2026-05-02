# 🧮 Pookie Calculator

A cute and functional **GUI-based calculator** built with Python and CustomTkinter, developed as part of the **CodSoft Python Programming Internship** (Task 2).

---

## ✨ Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Backspace (`⌫`) and clear (`C`) support
- **Calculation History** — view all past calculations in a scrollable panel
- **Clear History** — delete all history with one tap
- Smooth **screen navigation** between Calculator and History views
- Custom pink/rose themed UI built with `customtkinter`

---

## 📸 Preview

> Run the app locally to see the UI in action!

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| CustomTkinter | Modern GUI framework |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed. Then install the dependency:

```bash
pip install customtkinter
```

### Run the App

```bash
python calculator.py
```

---

## 📁 Project Structure

```
CODSOFT/
└── Task2-Calculator/
    └── calculator.py
```

---

## 💡 How It Works

1. **Input Expression** — tap number and operator buttons to build an expression
2. **Evaluate** — press `=` to compute the result using Python's `eval()`
3. **History** — every successful calculation is saved and viewable in the History tab
4. **Navigate** — use the bottom nav buttons (🧮 / 🕰) to switch views

---

## ⚠️ Known Limitations

- Uses `eval()` for expression parsing — suitable for personal/learning projects
- `%` button is present in UI but not yet functionally implemented
- No keyboard input support (mouse/touch only)

---

## 🔮 Future Improvements

- [ ] Refactor into a class-based OOP structure
- [ ] Replace `eval()` with a safe expression parser
- [ ] Add keyboard input support
- [ ] Implement percentage calculation
- [ ] Add light/dark theme toggle

---

## 👩‍💻 Author

Built with 💖 as part of the **CodSoft Python Programming Internship**

---

## 📌 Tags

`#codsoft` `#internship` `#python` `#gui` `#customtkinter` `#calculator`
