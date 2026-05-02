from datetime import datetime
import json
import customtkinter as ctk
from tkcalendar import DateEntry
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class Todo:
    def __init__(self):
        self.tasks=self.load_tasks()
        self.check_deadlines()
    def sort_tasks(self):
        self.tasks.sort(key=lambda task:
                       datetime.strptime(
                           task['deadline'],
                           "%d-%m-%Y"
                       ))
        self.save_tasks()
    def check_deadlines(self):
        current_date = datetime.today().date()
        for task in self.tasks:
            dd = datetime.strptime(task["deadline"], "%d-%m-%Y").date()
            days_left = (dd - current_date).days
            if days_left < 0:
                task["warning"] = "Overdue"
            elif days_left <= 2:
                task["warning"] = "Near Deadline"
            else:
                task["warning"] = ""
    def save_tasks(self):
        with open("tasks.json","w") as f:
            json.dump(self.tasks,f,indent=4)
    def load_tasks(self):
        try:
            with open("tasks.json","r")as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return[]
    def refresh_deadlines(self):
        self.check_deadlines()
app=ctk.CTk()
app.geometry("1000x600")
app.title("Todo App")
app.configure(fg_color="#f7f4ef")

"""
addinf left side bars 
"""
sidebar=ctk.CTkFrame(app,width=215,corner_radius=50,fg_color="#dce8d5")
sidebar.pack(side="left",fill="y",padx=15,pady=15)
sidebar.pack_propagate(False)
# main Frame:
main_frame=ctk.CTkFrame(app,corner_radius=0,fg_color="#f7f4ef")
main_frame.pack(side="right",fill="both",expand=True)
lab1=ctk.CTkLabel(sidebar,text="TODO LIST 🍃",font=("gaudgi",25,"bold"),text_color="#29592a")
lab1.pack(pady=(30,5))
lab2=ctk.CTkLabel(
    sidebar,
    text="Cozy Productivity",
    font=("Arial",14),
    text_color="#5f7a65"
)
lab2.pack(pady=(0,15),padx=(0,50))
"""
button creation:
"""
dashboard=ctk.CTkButton(sidebar,
                        text=" 📊 Dashboard ",
                        font=("Arial",16),
                        text_color="#29592a",
                        fg_color="#dce8d5",
                        height=40,
                        hover_color="#6b8560",
                        corner_radius=15,
                        anchor='w'
)
dashboard.pack(fill="x",padx=(6,18),pady=(5,5))
alltask=ctk.CTkButton(sidebar,
                      text=" 📋 All Tasks ",
                        font=("Arial",16),
                        text_color="#29592a",
                        fg_color="#dce8d5",
                        height=40,
                        hover_color="#6b8560",
                        corner_radius=15,
                        anchor='w')
alltask.pack(fill="x",padx=(6,18),pady=(5,5))
pendingtask=ctk.CTkButton(sidebar,
                        text=" ⏳ Pending Tasks",
                        font=("Arial",16),
                        text_color="#29592a",
                        fg_color="#dce8d5",
                        height=40,
                        hover_color="#6b8560",
                        corner_radius=15,
                        anchor="w")
pendingtask.pack(fill="x",padx=(6,18),pady=10)
exit=ctk.CTkButton(
    sidebar,
    text=" ⌫ Exit",
    font=("Arial",16),
    text_color="#f7f4ef",
    fg_color="#B08968",
    hover_color="#9C6644",  
    height=40,
    corner_radius=15,
    command=app.destroy
)
exit.pack(
    side="bottom",
    fill="x",
    padx=(20,20),
    pady=(0,30)
)
"""
main frame adjustment
"""
top_frame=ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)
top_frame.pack(
    fill="x",
    padx=40,
    pady=(35,10)
)
title=ctk.CTkLabel(
    top_frame,
    text="Stay Organized 🌿",
    font=("Georgia",30,"bold"),
    text_color="#29592a"
)
title.pack(side="left")
def set_quote(text):
    deadline_title.configure(text=text)
quote=ctk.CTkLabel(
    main_frame,
    text="Take a deep breath and start fresh today ☕",
    font=("Lucida Handwriting",16,"italic"),
    text_color="#8b6f5a"
)
quote.pack(anchor="nw",
    padx=42,
    pady=(0,10))
search_btn=ctk.CTkButton(
            top_frame,
            text="🔍 Search Task",
            font=("Arial",14,"bold"),
            width=150,
            height=40,
            fg_color="#d8c3b3",
            hover_color="#c4aa98",
            text_color="#5c4033",
            corner_radius=15,
    )
add_btn=ctk.CTkButton(
    app,
    text="+",
    font=("Arial",30,"bold"),
    width=50,
    height=50,
    corner_radius=100,
    fg_color="#7c9466",
    hover_color="#6b8560",
    text_color="white"
)
add_btn.place(
    relx=0.90,
    rely=0.88
)
"""
Deadline Session
"""
line=ctk.CTkFrame(
    main_frame,
    height=2,
    fg_color="#d8c3b3"
)
line.pack(
    fill="x",
    padx=40,
    pady=(15,10)
)
deadline_title=ctk.CTkLabel(main_frame,
                            text="⚠ Near Deadlines",
                            font=("Georgia",22,"bold"),
                            text_color="#5c4033")
deadline_title.pack(anchor="nw",padx=40,pady=(10,15))
deadline_frame=ctk.CTkScrollableFrame(
    main_frame,
    width=700,
    height=250,
    fg_color="#efe6dc",
    corner_radius=20
)
deadline_frame.pack(
    fill="both",
    padx=40,
    pady=(0,20)
)
def show_all_task_gui():
    for w in deadline_frame.winfo_children():
        w.destroy()
    set_quote("📋 Everything organized in one place")
    for task in t.tasks:
        create_task_frame(task)
def create_task_frame(task):
            card=ctk.CTkFrame(
                deadline_frame,
                fg_color="#f7f4ef",
                corner_radius=15,
                height=90
            )
            card.pack(fill="x",padx=15,pady=10)
            main_card=ctk.CTkFrame(
                card,
                fg_color="transparent"
            )
            main_card.pack(fill="x",padx=15,pady=15)
            text_frame=ctk.CTkFrame(
                main_card,
                fg_color="transparent"
            )
            text_frame.pack(side="left",anchor="w")
            ctk.CTkLabel(
                text_frame,
                text=f"Task: {task['name']}",
                text_color="#5c4033",
                font=("Poppins",16,"bold")
            ).pack(anchor="w")
            ctk.CTkLabel(
                text_frame,
                text=f"Deadline: {task['deadline']}",
                text_color="#7a5c48",
                font=("Poppins",13)
            ).pack(anchor="w")
            ctk.CTkLabel(
                text_frame,
                text=f"Status: {task['status']}",
                text_color="#7c9466",
                font=("Poppins",13,"bold")
            ).pack(anchor="w")
            extra_frame=ctk.CTkFrame(
                text_frame,
                fg_color="transparent"
            )
            extra_frame.pack(anchor="w",pady=(5,0))
            priority_tab=ctk.CTkLabel(
                extra_frame,
                text=f" {task['priority']} ",
                fg_color="#d8c3b3",
                text_color="#5c4033",
                corner_radius=10,
                font=("Poppins",11,"bold"),
                padx=10,
                pady=2
            )
            priority_tab.pack(side="left",padx=(0,8))
            category_tab=ctk.CTkLabel(
                extra_frame,
                text=f" {task['category']} ",
                fg_color="#cfe0c3",
                text_color="#29592a",
                corner_radius=10,
                font=("Poppins",11,"bold"),
                padx=10,
                pady=2
            )
            category_tab.pack(side="left")
            btn_frame=ctk.CTkFrame(
                main_card,
                fg_color="transparent"
            )
            btn_frame.pack(side="right")
            toggle_btn = ctk.CTkButton(
                        btn_frame,
                        text="✔",
                        width=36,
                        height=36,
                        fg_color="#a3b18a",
                        hover_color="#7c9466",
                        command=lambda t=task: toggle_task_status(t)
            )
            toggle_btn.pack(side="left", padx=2)
            edit_btn=ctk.CTkButton(
                btn_frame,
                text="✏️",
                width=36,
                height=36,
                corner_radius=12,
                fg_color="#d8c3b3",
                text_color="black",
                hover_color="#c4aa98",
                font=("Arial",16),
                command=lambda t=task:update_window(t)
            )
            edit_btn.pack(side="left",padx=(0,2))
            delete_btn=ctk.CTkButton(
                btn_frame,
                text=" 🗑 ",
                width=36,
                height=36,
                corner_radius=12,
                fg_color="#e6cfc3",
                hover_color="#d9b8aa",
                text_color="black",
                font=("Arial",16),
                command=lambda t=task:delete_window(t)
            )
            delete_btn.pack(side="left",padx=(2,0))
def toggle_task_status(task):
    if task["status"] == "Completed":
        task["status"] = "Pending"
    else:
        task["status"] = "Completed"
    t.save_tasks()
    show_all_task_gui()
def show_pending_gui():
    for w in deadline_frame.winfo_children():
        w.destroy()
    set_quote("⏳ Pending mode: Let's complete tasks")
    found=False
    for task in t.tasks:
        if task["status"]=="Pending":
            found=True
            create_task_frame(task)
    if found==False:
        ctk.CTkLabel(
            deadline_frame,
            text="No Pending Tasks 🌿",
            text_color="#5c4033",
            font=("Gaudgi",15,"bold")
        ).pack(pady=20)
def load_dashboard():
    for w in deadline_frame.winfo_children():
        w.destroy()
    set_quote("⚠ Focus on urgent deadlines today")
    found=False
    for task in t.tasks:
        if task["status"] == "Completed":
            continue
        deadline = datetime.strptime(task["deadline"], "%d-%m-%Y").date()
        current_date = datetime.today().date()
        days_left = (deadline - current_date).days
        if days_left <= 2:
            found = True
            if days_left < 0:
                msg = f"⚠ {task['name']}\nOverdue by {abs(days_left)} days"
            elif days_left == 0:
                msg = f"⚠ {task['name']}\nDue Today"
            else:
                msg = f"⚠ {task['name']}\nDue: {task['deadline']} ({days_left} days left)"
            card = ctk.CTkFrame(deadline_frame, fg_color="#f7f4ef")
            card.pack(fill="x", padx=15, pady=10)
            ctk.CTkLabel(
                card,
                text=msg,
                text_color="#5c4033",
                font=("Poppins", 14, "bold")
            ).pack(anchor="w", padx=10, pady=10)
    if not found:
        ctk.CTkLabel(
            deadline_frame,
            text="No tasks near deadline 🌿",
            text_color="#5c4033",
            font=("Poppins", 14, "bold")
        ).pack(pady=20)
def add_window():
    addw=ctk.CTkToplevel(app)
    addw.geometry("400x600")
    addw.title("Add Task")
    addw.configure(fg_color="#f7f4ef")
    addw.transient(app)
    addw.lift()
    addw.focus()
    addw.attributes("-topmost",True)
    ctk.CTkLabel(
                addw,
                text="────୨ৎ──── Add New Task ────୨ৎ────",
                font=("Gerogia",24,"bold"),
                text_color="#29592a"
                ).pack(pady=20)
    task_name=ctk.CTkEntry(
        addw,
        placeholder_text="Enter task name",
        width=300,
        height=40,
        fg_color="#f1e3d3",
        border_color="#c7a98d",
        text_color="#5c4033"
    )
    task_name.pack(pady=10)
    desp_entry=ctk.CTkEntry(
        addw,
        placeholder_text="Enter task description",
        width=300,
        height=40,
    fg_color="#f1e3d3",
    border_color="#c7a98d",
    text_color="#5c4033"
    )
    desp_entry.pack(pady=10)
    date_frame=ctk.CTkFrame(
        addw,
        fg_color="#f1e3d3",
        corner_radius=12,
        width=300,
        height=45
    )
    date_frame.pack(pady=10)
    deadline_entry=DateEntry(
        date_frame,
        width=18,
        background="#8b6f5a",
        foreground="white",
        headersbackground="#8b6f5a",
        normalbackground="#f7f4ef",
        weekendbackground="#efe6dc",
        selectbackground="#7c9466",
        borderwidth=0,
        date_pattern="dd-mm-y"
        )
    deadline_entry.pack(padx=10,pady=8)
    priority_menu=ctk.CTkOptionMenu(
        addw,
        values=["High","Medium","Low"],
        width=300,
        fg_color="#c7a98d",
        button_color="#8b6f5a",
        button_hover_color="#7a5c48",
        text_color="white"
    )
    priority_menu.pack(pady=10)
    category_entry=ctk.CTkEntry(
        addw,
        placeholder_text="Category",
        width=300,
        height=40,
        fg_color="#f1e3d3",
        border_color="#c7a98d",
        text_color="#5c4033"
    )
    category_entry.pack(pady=10)
    stauts_menu=ctk.CTkOptionMenu(
        addw,
        values=["Pending","Completed"],
        width=300,
        fg_color="#c7a98d",
        button_color="#8b6f5a",
        button_hover_color="#7a5c48",
        text_color="white"
    )
    stauts_menu.pack(pady=10)
    def save_gui_task():
        name=task_name.get().title()
        desp=desp_entry.get().title()
        dd=deadline_entry.get()
        category=category_entry.get().title()
        priority=priority_menu.get()
        status=stauts_menu.get()
        if name.strip()=="":
            error_label.configure(text="Task name cannot be empty!")
            return
        try:
            datetime.strptime(dd,"%d-%m-%Y")
        except ValueError:
            error_label.configure(text="Invalid date format!")
            return
        current_date=datetime.today()
        task={
            "id":len(t.tasks)+1,
            "name":name,
            "description":desp,
            "deadline":dd,
            "category":category,
            "priority":priority,
            "created_date":current_date.strftime("%d-%m-%Y"),
            "status":status
        }
        t.tasks.append(task)
        t.refresh_deadlines()
        t.save_tasks()
        load_dashboard()
        addw.destroy()
    error_label=ctk.CTkLabel(
        addw,
        text="",
        text_color="red",
        font=("Poppins",12,"bold")
    )
    error_label.pack(pady=(5,0))
    save_btn=ctk.CTkButton(
        addw,
        text="Save Task ✔",
        width=300,
        height=45,
        font=("Poppins",16,"bold"),
        corner_radius=25,
        fg_color="#8aa06f",
        hover_color="#74885d",
        command=save_gui_task
    ).pack(pady=25)
def delete_window(task):
    t.tasks.remove(task)
    for index,task in enumerate(t.tasks,start=1):
        task["id"]=index
    t.refresh_deadlines()
    t.save_tasks()
    show_all_task_gui()
def update_window(task):
    updatew=ctk.CTkToplevel(app)
    updatew.geometry("400x500")
    updatew.title("Update Task")
    updatew.configure(fg_color="#f7f4ef")
    updatew.transient(app)
    updatew.lift()
    updatew.focus()    
    ctk.CTkLabel(
        updatew,
        text="────୨ৎ──── Update Task ────୨ৎ────",
        font=("Georgia",22,"bold"),
        text_color="#8b6f5a"
    ).pack(pady=20)
    task_name=ctk.CTkEntry(
        updatew,
        width=300,
        height=40,
        fg_color="#f1e3d3",
        border_color="#c7a98d",
        text_color="#5c4033"
    )
    task_name.insert(0,task["name"])
    task_name.pack(pady=10)
    desp_entry=ctk.CTkEntry(
    updatew,
        width=300,
        height=40,
        fg_color="#f1e3d3",
        border_color="#c7a98d",
        text_color="#5c4033"
    )
    desp_entry.insert(0,task["description"])
    desp_entry.pack(pady=10)
    category_entry=ctk.CTkEntry(
        updatew,
        width=300,
        height=40,
        fg_color="#f1e3d3",
        border_color="#c7a98d",
        text_color="#5c4033"  
    )
    category_entry.insert(0,task["category"])
    category_entry.pack(pady=10)
    date_frame=ctk.CTkFrame(
        updatew,
        fg_color="#f1e3d3",
        corner_radius=12,
        width=300,
        height=45
        )
    date_frame.pack(pady=10)
    deadline_entry=DateEntry(
        date_frame,
        width=18,
        background="#8b6f5a",
        foreground="white",
        headersbackground="#8b6f5a",
        normalbackground="#f7f4ef",
        weekendbackground="#efe6dc",
        selectbackground="#7c9466",
        borderwidth=0,
        date_pattern="dd-mm-y"
    )
    deadline_entry.pack(padx=10,pady=8)
    deadline_entry.set_date(
    datetime.strptime(task["deadline"], "%d-%m-%Y")
    )
    priority_menu=ctk.CTkOptionMenu(
        updatew,
        values=["High","Medium","Low"],
        width=300,
        fg_color="#c7a98d",
        button_color="#8b6f5a",
        button_hover_color="#7a5c48",
        text_color="white"
    )
    priority_menu.set(task["priority"])
    priority_menu.pack(pady=10)
    status_menu=ctk.CTkOptionMenu(
        updatew,
        values=["Pending","Completed"],
        width=300,
        fg_color="#c7a98d",
        button_color="#8b6f5a",
        button_hover_color="#7a5c48",
        text_color="white"
    )
    status_menu.set(task["status"])
    status_menu.pack(pady=10)
    def save_uploaded_info():
        task["name"]=task_name.get().title()
        task["category"]=category_entry.get().title()
        task["deadline"]=deadline_entry.get()
        task["priority"]=priority_menu.get()
        task["status"]=status_menu.get()
        task["description"]=desp_entry.get().title()
        t.refresh_deadlines()
        t.save_tasks()
        show_all_task_gui()
        updatew.destroy()
    save_btn=ctk.CTkButton(
        updatew,
        text="Save Changes",
        width=300,
        height=45,
        fg_color="#8b6f5a",
        hover_color="#6d5747",
        command=save_uploaded_info
        )
    save_btn.pack(pady=20)
def search_window():
    searchw=ctk.CTkToplevel(app)
    searchw.geometry("350x250")
    searchw.title("Search Task")
    searchw.configure(fg_color="#f7f4ef")
    searchw.transient(app)
    searchw.lift()
    searchw.focus()
    ctk.CTkLabel(
        searchw,
        text="╰┈➤ˎˊ˗ Search Your Task 🔍",
        font=("Georgia",22,"bold"),
        text_color="#5c4033"
    ).pack(pady=20)

    search_entry=ctk.CTkEntry(
        searchw,
        placeholder_text="Enter task name",
        width=250,
        height=40,
        fg_color="#f1e3d3",
        border_color="#c7a98d",
        text_color="#5c4033"
    )
    search_entry.pack(pady=10)
    search_entry.bind("<Return>",lambda e: search_task_gui())
    def search_task_gui():
        name=search_entry.get().strip().lower()
        for w in deadline_frame.winfo_children():
            w.destroy()
        set_quote("🌿 Finding the task you're looking for")   
        found=False
        for task in t.tasks:
            if name in task["name"].lower():
                found=True
                create_task_frame(task)
        if found==False:
            ctk.CTkLabel(
                deadline_frame,
                text="No matching task found 🌿",
                text_color="#5c4033",
                font=("Poppins",14,"bold")
            ).pack(pady=20)
        searchw.destroy()
    search_task_btn=ctk.CTkButton(
        searchw,
        text="Search 🔍",
        width=250,
        height=42,
        fg_color="#8aa06f",
        hover_color="#74885d",
        text_color="white",
        corner_radius=20,
        font=("Poppins",15,"bold"),
        command=search_task_gui
    )
    search_task_btn.pack(pady=20)
search_btn.pack(side="right")
search_btn.configure(command=search_window)
alltask.configure(command=show_all_task_gui)
pendingtask.configure(command=show_pending_gui)
dashboard.configure(command=load_dashboard)
add_btn.configure(command=add_window)
t=Todo()
t.refresh_deadlines()
t.sort_tasks()
load_dashboard()
app.mainloop()
