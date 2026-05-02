# 🦢 SwanCrypt — Password Generator

A beautiful and secure **GUI-based Password Generator** built with Python and CustomTkinter, developed as part of the **CodSoft Python Programming Internship** (Task 3).

> *"Securely floating through the digital lake"* 🌊

---

## ✨ Features

- 🔐 **Generate Passwords** — based on user-defined length and strength
- 💪 **3 Strength Levels** — Weak, Medium, and Strong character sets
- 📊 **Visual Strength Bar** — colour-coded bars update in real time
- 📋 **One-Click Copy** — copies password directly to clipboard
- ⚠️ **Input Validation** — catches invalid input with friendly error messages
- 🌙 **Dark / Light Mode Toggle** — switch themes instantly with one button
- 🎨 **Clean Swan-themed UI** — soft blue palette with elegant typography

---

## 📸 Preview

> Run the app locally to see SwanCrypt in action!

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| CustomTkinter | Modern GUI framework |
| `random` | Password randomization |
| `string` | Character set library |

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install customtkinter
```

### Run the App

```bash
python password_generator.py
```

---

## 📁 Project Structure

```
CODSOFT/
└── Task3-PasswordGenerator/
    └── password_generator.py
```

---

## 💡 How It Works

### Strength Levels

| Level | Characters Used |
|-------|----------------|
| Weak | Lowercase letters only (a-z) |
| Medium | Uppercase + Lowercase + Digits (a-zA-Z0-9) |
| Strong | All of the above + Symbols (!@#$%...) |

### Steps
1. Enter your desired password **length** (minimum 8)
2. Select a **strength level** — Weak, Medium, or Strong
3. Click **Generate Password** to create your password
4. Hit the **📋 copy button** to copy it to clipboard

---

## ⚠️ Known Limitations

- Minimum password length is 8 characters
- No password history or save feature
- Clipboard may clear after app closes (OS dependent)

---

## 🔮 Future Improvements

- [ ] Wrap into a class-based structure
- [ ] Add password history log
- [ ] Add custom character inclusion/exclusion options
- [ ] Export password to a text file
- [ ] Add a length slider in addition to manual input

---

## 👩‍💻 Author

Built with 🦢 as part of the **CodSoft Python Programming Internship**

---

## 📌 Tags

`#codsoft` `#internship` `#python` `#gui` `#customtkinter` `#passwordgenerator` `#swancrypt`
