# 🦢 SwanCrypt — Password Generator

> Started as a simple terminal script — then upgraded to a full swan-themed GUI! 💻✨

*"Securely floating through the digital lake"* 🌊

---

## 📁 Versions

| Version | File | Type |
|---------|------|------|
| 🖥️ Terminal | `password_terminal.py` | Command Line |
| 🎨 GUI | `password_generator.py` | CustomTkinter |

---

## 🖥️ Terminal Version

### ✨ Features
- Enter desired password length
- Validates minimum length of 8
- Generates random password using letters + digits
- Displays password instantly

### 🚀 Run Terminal Version

```bash
python password_terminal.py
```

### 💡 Core Logic

```python
char = string.ascii_letters + string.digits
passw = "".join(random.choices(char, k=passl))
```

Just 2 lines — that's the heart of every password generator! 🔐

---

## 🎨 GUI Version — SwanCrypt

### ✨ Features

- 🔐 **Generate Passwords** — based on user-defined length and strength
- 💪 **3 Strength Levels** — Weak, Medium, Strong character sets
- 📊 **Visual Strength Bar** — colour-coded bars update in real time
- 📋 **One-Click Copy** — copies password directly to clipboard
- ⚠️ **Input Validation** — catches invalid input with friendly messages
- ↻ **Refresh Button** — clears input and resets everything to default
- 🎨 **Swan-themed UI** — soft blue palette with elegant typography

### Strength Levels

| Level | Characters Used |
|-------|----------------|
| Weak | Lowercase only (a-z) |
| Medium | Uppercase + Lowercase + Digits |
| Strong | All of the above + Symbols (!@#$%) |

### 🚀 Run GUI Version

```bash
pip install customtkinter
python password_generator.py
```

---

## 🔮 Why I Upgraded to GUI

After building the terminal version I realised:
- No way to choose strength level
- No visual feedback on password quality
- Copy-paste was manual and annoying
- Needed a strength bar to show how secure the password is 😄

So I built SwanCrypt — same core logic, completely new experience!

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| CustomTkinter | GUI framework |
| `random` | Password randomization |
| `string` | Character set library |

---

## 📁 Project Structure

```
CODSOFT/
└── Task3-PasswordGenerator/
    ├── password_terminal.py
    ├── password_generator.py
    └── README.md
```

---

## 👩‍💻 Author

Built with 🦢 as part of the **CodSoft Python Programming Internship**

---

## 📌 Tags

`#codsoft` `#internship` `#python` `#gui` `#terminal` `#customtkinter` `#passwordgenerator` `#swancrypt``#passwordgenerator` `#swancrypt`
