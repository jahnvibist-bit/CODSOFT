import customtkinter as ctk
import random
import string
ctk.set_appearance_mode("light")
root=ctk.CTk()
root.geometry("1000x600")
root.title("SwanCrypt")
root.configure(fg_color="#EAF4FF")
def pass_gen(passl,strength):
    if strength=="Weak":
        chars=string.ascii_lowercase
    elif strength=="Medium":
        chars=string.ascii_letters+string.digits
    else:
        chars=string.ascii_letters+string.digits+string.punctuation

    return "".join(random.choices(chars,k=passl))
def update_strength(level):
    weak_bar.configure(fg_color="#D9E6F2")
    medium_bar.configure(fg_color="#D9E6F2")
    strong_bar.configure(fg_color="#D9E6F2")
    if level=="Weak":
        weak_bar.configure(fg_color="#FF6B6B")
        strength_label.configure(text="Password Strength • Weak 🔴")
    elif level=="Medium":
        weak_bar.configure(fg_color="#FFD93D")
        medium_bar.configure(fg_color="#FFD93D")
        strength_label.configure(text="Password Strength • Medium 🟡")
    else:
        weak_bar.configure(fg_color="#6BCB77")
        medium_bar.configure(fg_color="#6BCB77")
        strong_bar.configure(fg_color="#6BCB77")
        strength_label.configure(text="Password Strength • Strong 🟢")
def select_strength(level):
    strength_var.set(level)
    update_strength(level)
def create_password():
    try:
        length=int(length_entry.get())
        if length<8:
            error_label.configure(
                text="⚠ Length must be at least 8",
                text_color="red"
            )
            output_label.configure(
                text="Your password will appear here"
            )
            return
        strength=strength_var.get()
        password=pass_gen(length,strength)
        output_label.configure(
            text=f"🔐 {password}"
        )
        error_label.configure(text="")
        update_strength(strength)
    except:
        error_label.configure(
            text="⚠ Enter a valid number!",
            text_color="red"
        )
        output_label.configure(
            text="Your password will appear here"
        )
def copy_password():
    password=output_label.cget("text")
    if password!="Your password will appear here":
        root.clipboard_clear()
        root.clipboard_append(password)
        error_label.configure(
            text="✔ Password copied successfully!",
            text_color="#4CAF50"
        )
def toggle_mode():
    current=ctk.get_appearance_mode()
    if current=="Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")
main_frame=ctk.CTkFrame(
    root,
    fg_color="#FAFCFF",
    corner_radius=28,
    border_width=2,
    border_color="#A9C9EE"
)
main_frame.pack(
    padx=45,
    pady=35,
    fill="both",
    expand=True
)
top_frame=ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)
top_frame.pack(
    fill="x",
    padx=30,
    pady=(20,10)
)
title=ctk.CTkLabel(
    top_frame,
    text="°‧ 𓆝 𓆟 𓆞 ·｡ S W A N C R Y P T ⋆.˚🦢⋆",
    text_color="#1B3651",
    font=("Cormorant Garamond",34,"bold")
)
title.pack(
    pady=(8,6)
)
quote=ctk.CTkLabel(
    top_frame,
    text="securely floating through the digital lake",
    font=("Georgia",17,"italic"),
    text_color="#6B7C93"
)
quote.pack(
    pady=(0,2),padx=(60,0)
)
def refresh_app():
    length_entry.delete(0,"end")
    output_label.configure(
        text="Your password will appear here"
    )
    error_label.configure(text="")
    strength_var.set("Medium")
    update_strength("Medium")
refresh_btn=ctk.CTkButton(
    top_frame,
    text="↻",
    width=42,
    height=42,
    corner_radius=22,
    fg_color="#DCEEFF",
    hover_color="#B8D8F8",
    text_color="#1B3651",
    font=("Arial",20,"bold"),
    command=refresh_app
)
refresh_btn.place(relx=0.90,rely=0.05)
middle_frame=ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)
middle_frame.pack(
    pady=(15,20)
)
length_entry=ctk.CTkEntry(
    middle_frame,
    placeholder_text="Enter password length",
    width=280,
    height=48,
    corner_radius=18,
    fg_color="#EAF4FF",
    border_color="#B8D8F8",
    border_width=2,
    text_color="#1B3651",
    placeholder_text_color="#7A92A8",
    font=("Poppins",15)
)
length_entry.pack(
    pady=(10,18)
)
strength_var=ctk.StringVar(value="Medium")
strength_label=ctk.CTkLabel(
    middle_frame,
    text="Password Strength • Medium 🟡",
    font=("Poppins",16),

)
strength_label.pack(
    pady=(0,10)
)
bar_frame=ctk.CTkFrame(
    middle_frame,
    fg_color="transparent"
)
bar_frame.pack(
    pady=(0,18)
)
weak_bar=ctk.CTkFrame(
    bar_frame,
    width=85,
    height=16,
    corner_radius=10,
    fg_color="#FFD93D"
)
weak_bar.pack(
    side="left",
    padx=5
)
medium_bar=ctk.CTkFrame(
    bar_frame,
    width=85,
    height=16,
    corner_radius=10,
    fg_color="#FFD93D"
)
medium_bar.pack(
    side="left",
    padx=5
)
strong_bar=ctk.CTkFrame(
    bar_frame,
    width=85,
    height=16,
    corner_radius=10,
    fg_color="#D9E6F2"
)
strong_bar.pack(
    side="left",
    padx=5
)
btn_frame=ctk.CTkFrame(
    middle_frame,
    fg_color="transparent"
)
btn_frame.pack(
    pady=(0,22)
)
weak_btn=ctk.CTkButton(
    btn_frame,
    text="Weak",
    width=95,
    height=42,
    corner_radius=18,
    fg_color="#FFB3B3",
    hover_color="#FF6B6B",
    text_color="#3A3A3A",
    font=("Poppins",14,"bold"),
    command=lambda:select_strength("Weak")
)
weak_btn.pack(
    side="left",
    padx=6
)
medium_btn=ctk.CTkButton(
    btn_frame,
    text="Medium",
    width=95,
    height=42,
    corner_radius=18,
    fg_color="#FFE69A",
    hover_color="#FFD93D",
    text_color="#3A3A3A",
    font=("Poppins",14,"bold"),
    command=lambda:select_strength("Medium")
)
medium_btn.pack(
    side="left",
    padx=6
)
strong_btn=ctk.CTkButton(
    btn_frame,
    text="Strong",
    width=95,
    height=42,
    corner_radius=18,
    fg_color="#B9FBC0",
    hover_color="#6BCB77",
    text_color="#3A3A3A",
    font=("Poppins",14,"bold"),
    command=lambda:select_strength("Strong")
)
strong_btn.pack(
    side="left",
    padx=6
)
generate_btn=ctk.CTkButton(
    middle_frame,
    text="Generate Password ⁠♡",
    width=250,
    height=50,
    corner_radius=24,
    fg_color="#7DA0C4",
    hover_color="#5A7A99",
    text_color="white",
    font=("Poppins",16,"bold"),
    command=create_password
)
generate_btn.pack(
    pady=(0,24)
)
output_frame=ctk.CTkFrame(
    middle_frame,
    fg_color="transparent"
)
output_frame.pack(
    pady=(0,14)
)
output_label=ctk.CTkLabel(
    output_frame,
    text="Your password will appear here",
    width=390,
    height=58,
    corner_radius=18,
    fg_color="#DCEEFF",
    text_color="#1B3651",
    font=("Poppins",16,"bold")
)
output_label.pack(
    side="left",
    padx=(0,12)
)
copy_btn=ctk.CTkButton(
    output_frame,
    text="📋",
    width=58,
    height=58,
    corner_radius=30,
    fg_color="#B8D8F8",
    hover_color="#7DA0C4",
    text_color="black",
    font=("Arial",20),
    command=copy_password
)
copy_btn.pack(
    side="left"
)
error_label=ctk.CTkLabel(
    middle_frame,
    text="",
    font=("Poppins",15,"bold"),
    text_color="red"
)
error_label.pack(pady=(5,0))
root.mainloop()
