#making calculator using gui
import customtkinter as ctk
exp=""
history=[]
def update_history():
    for w in hist_scrollbar.winfo_children():
        w.destroy()
    if len(history)==0:
        empty=ctk.CTkLabel(
            hist_scrollbar,
            text="No calculations yet ♡",
            font=("Arial",18),
            text_color="gray"
        )
        empty.pack(pady=20)
        return
    for item in history:
        lbl=ctk.CTkLabel(
            hist_scrollbar,
            text=item,
            font=("Gaudgi",18),
            text_color="#71203D",
            anchor="w"
        )
        lbl.pack(fill="x",pady=10,padx=5)
def click(v):
    global exp
    if v=="x":
        v="*"
    if v=="C":
        exp=""
        expr_label.configure(text="")
        result_label.configure(text="0")
        #screen.set("")
        return
    if v=="⌫":
        exp=exp[:-1]
        expr_label.configure(text=exp)
        return
    if v=="=":
        try:
            res=str(eval(exp))
            history.append(f"{exp.replace('*','x')} = {res}")
            result_label.configure(text=res)
            exp=res
            update_history()
           # screen.set(exp)
        except:
            result_label.configure(text="Error 💔")
           # screen.set("Error")
            exp=""
        return
    exp=exp+str(v)
    expr_label.configure(text=exp)
    #screen.set(exp)
"""
creating two fn to swtich windows
"""    
def showCalc():
    history_frame.pack_forget()
    calc_frame.pack(fill="both",expand=True)
def showHistory():
    calc_frame.pack_forget()
    history_frame.pack(fill="both",expand=True)
def clear_hist():
    history.clear()
    update_history()
root=ctk.CTk() # creates main window
#screen=ctk.StringVar()
root.title("Pookie Calculator")# displays title at top of window
root.geometry("300x500")# size of window]
root.configure(fg_color="#f8e8ee") # for setting background color
"""
creating one main frame
this will hold calc and history frames
"""
main_frame=ctk.CTkFrame(root,fg_color="#f8e8ee")
main_frame.pack(fill="both",expand=True)
"""
 screen will be divided in 3 parts
 top => display screen
 middle => buttons
 bottom =>  for naviagtion 
"""
calc_frame = ctk.CTkFrame(main_frame, fg_color="#f8e8ee")
calc_frame.pack(fill="both", expand=True)
t_frame=ctk.CTkFrame(calc_frame,fg_color="#e8bfc9",height=100,corner_radius = 20)
t_frame.pack(fill="x",pady=(5, 0),padx=(5,5)) # pack is for fill
m_frame=ctk.CTkFrame(calc_frame,fg_color="#f8e8ee",corner_radius = 0)
m_frame.pack(expand=True,fill="both") # both will fill both height and width expand=True takes u extra aspace
b_frame=ctk.CTkFrame(root,fg_color="#bb7782",height=50,corner_radius=0)
b_frame.pack(fill="x")
"""
creating buttons 
"""
buttons=[
    ["C","%","⌫","/"],
    ["7","8","9","x"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["00","0",".","="]
]
"""
buttons makiing and padding and all
"""
row=0
for i in buttons:
    col=0
    for j in i: # for each element inside
       if j in ["+", "-", "x", "/"]:
           fg="#71203D"
           text_color="white"
           hover_color="#d44e86"
       elif j in "=":
            fg="pink"
            text_color="#71203D"
            hover_color="#bc2d69"
       elif j in ["C","%","⌫"]:
           fg="#ad97a6"
           text_color="#71203D"
           hover_color="#BC8598"
       else:
           fg="#e2cdd8"
           text_color="black"
           hover_color="#85737b"
        
       button=ctk.CTkButton(m_frame,text=j,command=lambda v=j:click(v),width=50,height=50,fg_color=fg,text_color=text_color,hover_color=hover_color)
       button.grid(row=row,column=col,padx=9,pady=6,ipadx=3,ipady=3)
       col+=1
    row+=1
"""
now making screen
"""
expr_label = ctk.CTkLabel(
    t_frame,
    text="",
    text_color="gray",
    font=("Arial", 25)
)
expr_label.pack(anchor="e", padx=(2,15),pady=(2,0))
result_label = ctk.CTkLabel(
    t_frame,
    text="0",
    text_color="#ab2845",
    font=("Arial", 30)
)
result_label.pack(anchor="e", padx=20,pady=20)
"""
creating  freame for history
"""
history_frame=ctk.CTkFrame(main_frame,fg_color="#f8e8ee") 
"""
creating frame for hitory
"""
hist_top_frame=ctk.CTkFrame(
    history_frame,
    fg_color="#f4c9d8",
    corner_radius=15
)
hist_top_frame.pack(fill="x",padx=10,pady=10)
hist_title=ctk.CTkLabel(
    hist_top_frame,
    text="🕰 History",
    font=("Arial",24),
    text_color="#71203D"
)
hist_title.pack(side="left",padx=15)
"""
creating dustbin button 
"""
dustbin=ctk.CTkButton(
    hist_top_frame,
    text="🗑",
    height=40,
    width=40,
    corner_radius=80,
    fg_color="#ab2845",
    hover_color="#d35d84",
    command=clear_hist,
    font=("Arial",18)
)
dustbin.pack(side="right", padx=10)
"""
frame for history content
"""
hist_cont_frame=ctk.CTkFrame(
    history_frame,
    fg_color="#f8e8ee",
)
hist_cont_frame.pack(
    fill="both",
    expand=True,
    padx=5,
    pady=5
)
"""
scrollbar creation
"""
hist_scrollbar=ctk.CTkScrollableFrame(
    hist_cont_frame,
    fg_color="#f8e8ee"
)
hist_scrollbar.pack(
    fill="both",
    expand=True,
    padx=5,
    pady=5
)
calc_btn=ctk.CTkButton(
    b_frame,
    text="🧮",
    fg_color="#ab2845",
    command=showCalc,
    width=55,
    height=55,
    corner_radius=90,
    hover_color="#9f5976",
    text_color="#EEDFE4",
font=("Segoe UI Emoji",25)
)
calc_btn.pack(side="left", padx=30, pady=6)
history_btn=ctk.CTkButton(
    b_frame,
    text="⏳",
    fg_color="#ab2845",
    command=showHistory,
    width=55,
    height=55,
    corner_radius=90,
    hover_color="#9f5976",
    text_color="#EEDFE4",
    font=("Arial",30)
)
history_btn.pack(side="left", padx=25, pady=6)
update_history()
root.mainloop()
