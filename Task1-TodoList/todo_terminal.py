from datetime import datetime
import json
class Todo:
    def __init__(self):
        self.tasks=self.load_tasks()
        self.check_deadlines()
    def add_task(self):
        while True:
            name=input("Enter Name of the task: ").title()
            if name.strip()=="":
                print("Task name can not be empty!")
            else:
                break    
        desp=input("""Provide Task Description if any: """).title()
        while True:
            dd=input("Enter deadline for the task: ")
            try:
                deadline=datetime.strptime(dd,"%d-%m-%Y")
                break
            except ValueError:
                print("Invalid date format !")
        category=input("""Enter Category of your task
        eg: Coding | Studying | Gym | Personal : """).title()
        while True:
            priority=input("Set Priority of your task (eg.High | Medium | Low): ").title()
            if priority in ["High","Medium","Low"]:
                break
            else:
                print("Invalid Priority !")
        while True:
            status=input("Enter Status of your task (eg. Pending | completed ): ").title()
            if status in ["Pending","Completed"]:
                break
            else:
                print("Invalid Status !")
        current_date=datetime.today()
        days_left=(deadline-current_date).days 
        if days_left<0:
            print("Task Overdue!")
        elif days_left<=2:
            print("Task is near deadline !!")
        task={
            "id":len(self.tasks)+1,
            "name":name,
            "description":desp,
            "deadline":dd,
            "category":category,
            "priority":priority,
            "created_date": current_date.strftime("%d-%m-%Y"),
            "status":status
        }
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully")

    def delete_task(self):
        if len(self.tasks)==0:
            print("No task available!")
            return
        self.show_all_tasks()
        while True:
            try:
                id=int(input("Enter the task number to delete: "))                
                if 1<= id<=len(self.tasks):
                    confirm=input("Are you sure you want to delete this task? (y/n): ").lower()
                    if confirm=="y":
                        self.tasks.pop(id-1)
                        for index,task in enumerate(self.tasks,start=1):
                            task["id"]=index
                        self.save_tasks()
                        print("Task deleted successfully!")
                        return
                else:
                    print("Task deletion cancelled!")
                    return
            except ValueError:
                print("Please enter a valid number!")    

    def update_task(self):
        if len(self.tasks)==0:
            print("No task available!")
            return
        self.show_all_tasks()
        while True:
            try:
                choice=int(input("Enter the number of task you wanna update: "))
                if 1<=choice<=len(self.tasks):
                    task=self.tasks[choice-1]
                    while True:
                        up=int(input("""1. Update Name
                                        2. Update Deadline
                                        3. Update Priority
                                        4. Update Status
                                        5. Update Category
                                        6. Exit
                                        Enter choice: """))
                        match(up):
                            case 1:
                                while True:
                                    name=input("Enter new name of the task to update: ").title()
                                    if name.strip()=="":
                                        print("Task name cannot be empty!")
                                    else:
                                        task["name"]=name
                                        print("Task name updated!")
                                        self.save_tasks()
                                        return
                            case 2:
                                while True:
                                    dd=input("Enter deadline for the task (DD-MM-YYYY): ")
                                    try:
                                        deadline=datetime.strptime(dd,"%d-%m-%Y")
                                        task["deadline"]=dd
                                        print("Deadline updated!")
                                        self.save_tasks()
                                        return
                                    except ValueError:
                                        print("Invalid date format!")
                            case 3:
                                while True:
                                    priority=input("Set Priority (High | Medium | Low): ").title()
                                    if priority in ["High","Medium","Low"]:
                                        task["priority"]=priority
                                        print("Priority updated!")
                                        self.save_tasks()
                                        return
                                    else:
                                        print("Invalid Priority!")
                            case 4:
                                    while True:
                                        status=input("Enter Status (Pending | Completed): ").title()
                                        if status in ["Pending","Completed"]:
                                            task["status"]=status
                                            print("Status updated!")
                                            self.save_tasks()
                                            return
                                        else:
                                            print("Invalid Status!")
                            case 5:
                                category=input("""Enter Category of your task
                                                eg: Coding | Studying | Gym | Personal : """).title()
                                task["category"]=category
                                print("Category updated!")
                                self.save_tasks()
                                return
                            case 6:
                                self.save_tasks()
                                return
                            case _:
                                print("Invalid Input Entered!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter numbers only!")
    def search_task(self):
        name=input("Enter name of task you wanna search : ").title()
        found=False
        for i in self.tasks:
            if name==i["name"]:
                print(f"Task name: {i['name']}\tDeadline: {i['deadline']}\tPriority: {i['priority']}\tStatus:{i['status']}\tCategory: {i['category']}")
                found=True
                break
        if found==False:
            print(f"{name} task not found: ")

    def show_all_tasks(self):
        if len(self.tasks)==0:
            print("No tasks available!")
        else:
            for i, task in enumerate(self.tasks, start=1):
              print(f"Task ID:{task['id']} | Task Name:{task['name']}\tDeadline:{task['deadline']}\tPriority:{task['priority']}\tStatus:{task['status']}\tCategory:{task['category']}")
              print("-" * 128)
    def sort_tasks(self):
        self.tasks.sort(key=lambda task:
                       datetime.strptime(
                           task['deadline'],
                           "%d-%m-%Y"
                       ))
        
        self.save_tasks()
        print("Task sorted by deadline")

    def check_deadlines(self):
        current_date=datetime.today()
        for task in self.tasks:
            dd=datetime.strptime(task["deadline"],"%d-%m-%Y")
            days_left=(dd-current_date).days
            if days_left<0:
                print(f"task '{task['name']}' is Overdue!")
            elif days_left<=2:
                print(f"task '{task['name']}' is near deadline !!")

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
    def pending_task(self):
        if len(self.tasks)==0:
            print("No tasks Available!")
            return
        found=False
        for i in self.tasks:
            if i["status"]=="Pending":
                print(f"Task name: {i['name']}\tDeadline: {i['deadline']}\tPriority: {i['priority']}\tStatus:{i['status']}\tCategory: {i['category']}")
                found=True
        if found==False:
            print("No Pending Tasks!")
    def stats(self):
        total=len(self.tasks)
        completed=0
        pending=0
        for task in self.tasks:
            if task["status"]=="Completed":
                completed+=1
            else:
                pending+=1
        print(f"Total Tasks: {total}")
        print(f"Completed Tasks: {completed}")
        print(f"Pending Tasks: {pending}")
print("******* Welcome Todo List *******")
t=Todo()
while True:
    try:
        a=int(input("""Enter a number to perform a following task:
                    1. Add Task
                    2. Delete Task
                    3. Update Task
                    4. View All Task
                    5. Sort Task
                    6. Search Task
                    7. View Pending Task
                    8. View Task Status
                    9. Exit: """))
        match a:
            case 1:
                t.add_task()
                input("Press Enter to continue...")
            case 2:
                t.delete_task()
                input("Press Enter to continue...")
            case 3:
                t.update_task()
                input("Press Enter to continue...")
            case 4:
                t.show_all_tasks()
                input("Press Enter to continue...")
            case 5:
                t.sort_tasks()
                input("Press Enter to continue...")
            case 6:
                t.search_task()
                input("Press Enter to continue...")
            case 7:
                t.pending_task()
                input("Press Enter to continue...")
            case 8:
                t.stats()
                input("Press Enter to continue...")
            case 9:
                print("Exiting Todo App...")
                break
            case _:
                print("Invalid input enter!")
    except ValueError:
        print("Please enter numbers only")
