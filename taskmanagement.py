#imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Database_TaskManagement
import mysql.connector

tasks = []


class MainWindow:
    def __init__(self,master):
        self.master = master
        self.master.title("Task Management System")
        self.master.geometry('1280x650')
        self.master.config(bg = 'grey')
        self.master.resizable(0,0)
        
        self.title = Label(self.master, text="Task Management System", font = "Times 15 bold", fg="#fff", bg="grey")
        self.title.pack(side='top')
        
        self.tasks = []
        #Database Value
        self.entertask = StringVar()
        self.startdate = StringVar()
        self.enddate = StringVar()
        self.category = StringVar()
        self.priorityvar = StringVar()
        self.status = StringVar()
        
        #FramesforEntries
        self.frame = Frame(self.master, bg="#c0c0c0")
        self.frame.place(relwidth=0.88, relheight=0.18, relx=0.06, rely=0.10)
        
        self.frame1 = Frame(self.master, bg="grey")
        self.frame1.place(relwidth=0.88, relheight=0.10, relx=0.06, rely=0.85)
        
        self.frame2 = LabelFrame(self.master, bg="grey", text='Task Lists', bd = 5, font='Times 12 bold', fg="#fff")
        self.frame2.place(relwidth=0.88, relheight=0.55, relx=0.06, rely=0.29)
        
        #Labels and 
        self.EnterTaskLabel = Label(self.frame, text="Enter your task:", font='Times 10 bold', bg="#c0c0c0", fg='black')
        self.EnterTaskLabel.place(x=2, y=1)
        self.EnterTaskEntry = Entry(self.frame, width=35, font='Times 10', bd=2, textvariable=self.entertask)
        self.EnterTaskEntry.place(x=120, y=1)
        
        self.EnterDateLabel = Label(self.frame, text="Enter Start Date:\n(YYYY-MM-DD)", font='Times 10 bold', bg="#c0c0c0", fg='black')
        self.EnterDateLabel.place(x=2, y=30)
        self.EnterDateEntry = Entry(self.frame, width=35, font='Times 10', bd=2, textvariable=self.startdate)
        self.EnterDateEntry.place(x=120, y=30)
        
        self.EnterEndDateLabel = Label(self.frame, text="Enter End Date:\n(YYYY-MM-DD)", font='Times 10 bold', bg="#c0c0c0", fg='black')
        self.EnterEndDateLabel.place(x=2, y=60)
        self.EnterEndDateEntry = Entry(self.frame, width=35, font='Times 10', bd=2, textvariable=self.enddate)
        self.EnterEndDateEntry.place(x=120, y=60)
        
        self.CategoryLabel = Label(self.frame, text="Enter the Category:", font='Times 10 bold', bg="#c0c0c0", fg='black')
        self.CategoryLabel.place(x=2, y=90)
        self.CategoryEntry = ttk.Combobox(self.frame, textvariable=self.category, font='Times 10', values=["House Chores", "Academics", "Work", "Errands", "Others"], state="readonly", width=28)
        self.CategoryEntry.place(x=120, y=90)
        
        self.PriorityLabel = Label(self.frame, text="Level of Priority", font='Times 10 bold', bg="#c0c0c0", fg='black')
        self.PriorityLabel.place(x=360, y=1)
        self.PriorityEntry = ttk.Combobox(self.frame, textvariable=self.priorityvar, font='Times 10', values=["1 - Least Important", "2 - Medium Least", "3 - Medium", "4 - High", "5 - Urgent"], state="readonly", width=28)
        self.PriorityEntry.place(x=360, y=18)
        
        self.StatusLabel = Label(self.frame, text="Status", font='Times 10 bold', bg="#c0c0c0", fg='black')
        self.StatusLabel.place(x=360, y=70)
        self.StatusEntry = ttk.Combobox(self.frame, textvariable=self.status, font='Times 10', values=["Progressing", "Done", "Not yet done"], state="readonly", width=28)
        self.StatusEntry.place(x=360, y=90)

        #button for Add
        self.AddTaskButton = Button(self.frame,font = ('Times',10), text="Add the Task", height=1, width=20, fg="black", bg="lavender", command = self.addtask)
        self.AddTaskButton.place(x=650, y=90)
        
        #button for Update Task
        self.UpdateButton = Button(self.frame,font = ('Times',10), text="Update Task", height=1, width=20, fg="black", bg="lavender", command = self.updateData)
        self.UpdateButton.place(x=650, y=1)
        
        #button for Display Task
        self.DispButton = Button(self.frame,font = ('Times',10), text="Display Task", height=6, width=15, fg="black", bg="lavender", command = self.displayData)
        self.DispButton.place(x=825, y=9)
        
        self.Hide = Button(self.frame,font = ('Times',10), text="Hide Task", height=1, width=20, fg="black", bg="lavender", command = self.hideData)
        self.Hide.place(x=650, y=43)
        
        #button for Delete Category
        self.DelCatButton = Button(self.frame,font = ('Times',10), text="Delete Category", height=6, width=15, fg="black", bg="lavender", command = self.deleteData)
        self.DelCatButton.place(x=980, y=9)
        
        self.Exit = Button(self.frame1,font = ('Times',10), text="Exit", height=1, width=15, fg="white", bg="grey", command = self.exit)
        self.Exit.place(x=1000, y=18)
        
        #button for Help&Info
        self.HelpInfoButton = Button(self.frame1,font = ('Times',10), text="Help and Information", height=1, width=100, fg="white", bg="grey", command = self.help)
        self.HelpInfoButton.place(x=190, y=18)
        
        self.taskTree = ttk.Treeview(self.frame2, columns=("Task ID", "Task", "Start Date", "End Date", "Category", "Priority", "Status"), show="headings", height=12)
        self.taskTree.heading("Task ID", text="Task ID")
        self.taskTree.heading("Task", text="Task")
        self.taskTree.heading("Start Date", text="Start Date")
        self.taskTree.heading("End Date", text="End Date")
        self.taskTree.heading("Category", text="Category")
        self.taskTree.heading("Priority", text="Priority")
        self.taskTree.heading("Status", text="Status")
        
        self.taskTree.column("Task ID", width=50)
        self.taskTree.column("Task", width=200)
        self.taskTree.column("Start Date", width=120)
        self.taskTree.column("End Date", width=120)
        self.taskTree.column("Category", width=150)
        self.taskTree.column("Priority", width=80)
        self.taskTree.column("Status", width=100)

        self.taskTree.place(relwidth=1, relheight=1)
    
    def clear_entries(self):
        self.entertask.set("")  
        self.startdate.set("")  
        self.enddate.set("")  
        self.category.set("") 
        self.priorityvar.set("")
        self.status.set("")
    
    def exit(self):
        result = messagebox.askyesno("Terminating...", "Are you sure you want to exit?")
        if result:
            self.master.destroy()
    
    def addtask(self):
        try:
            if len(self.EnterTaskEntry.get()) == 0 or len(self.CategoryEntry.get()) == 0 or len(self.PriorityEntry.get()) == 0 or len(self.StatusEntry.get()) == 0:
                messagebox.showwarning("Input Error", "Please fill in all required fields: Task, Category, Priority, and Status.")
                return  empty

            entertask = self.EnterTaskEntry.get()
            startdate = self.EnterDateEntry.get()
            enddate = self.EnterEndDateEntry.get()
            category = self.CategoryEntry.get()
            priority = self.PriorityEntry.get()
            status = self.StatusEntry.get()

            task_id = Database_TaskManagement.addRec(entertask, startdate, enddate, category, priority, status)

            self.clearData()
            self.CategoryEntry.set('') 
            self.PriorityEntry.set('')  
            self.StatusEntry.set('')    

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to add record: {e}")


            
    def deleteData(self):
        try:
            selected_item = self.taskTree.selection()[0]
            task_id = self.taskTree.item(selected_item)["values"][0]  
            self.taskTree.delete(selected_item)

            Database_TaskManagement.deleteRec(task_id)

            messagebox.showinfo("Success", "Record deleted successfully!")
        except IndexError:
            messagebox.showerror("Error", "No record selected to delete.")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to delete record: {e}")
    
    def displayData(self):
        try:
            tasks = Database_TaskManagement.viewData()

            for item in self.taskTree.get_children():
                self.taskTree.delete(item)

            if not tasks:
                messagebox.showinfo("No Tasks", "There are no tasks to display.")
                return  

            for task in tasks:
                task_id, task_name, start_date, end_date, category, priority, status = task
                self.taskTree.insert("", "end", values=(task_id, task_name, start_date, end_date, category, priority, status))

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to retrieve data: {e}")
    
    def hideData(self):
        for row in self.taskTree.get_children():
            self.taskTree.delete(row)
    
    def clearData(self):
        self.EnterTaskEntry.delete(0, END)
        self.EnterDateEntry.delete(0, END)
        self.EnterEndDateEntry.delete(0, END)
        self.CategoryEntry.delete(0, END)
        self.PriorityEntry.delete(0, END)
        self.StatusEntry.delete(0, END)
    
    def updateData(self):
        try:
            selected_item = self.taskTree.selection()[0]
            task_id = self.taskTree.item(selected_item)["values"][0]  
            entertask = self.EnterTaskEntry.get()
            startdate = self.EnterDateEntry.get()
            enddate = self.EnterEndDateEntry.get()
            category = self.CategoryEntry.get()
            priority = self.PriorityEntry.get()
            status = self.StatusEntry.get()

            Database_TaskManagement.dataUpdate(task_id, entertask, startdate, enddate, category, priority, status)

            for item in self.taskTree.get_children():
                self.taskTree.delete(item)

            self.displayData()
            self.clearData()

            messagebox.showinfo("Success", "Record updated successfully!")

        except IndexError:
            messagebox.showerror("Error", "No record selected to update.")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to update record: {e}")
    

    def help(self):
        self.HelpWindow = Toplevel(self.master)
        self.app = HelpInfo(self.HelpWindow)
    
class HelpInfo:
    def __init__(self,master):
        self.master = master
        self.master.title("Help and Information Desk")
        self.master.geometry('1000x500+270+70')
        self.master.config(bg = 'grey')
        self.master.resizable(0,0)
        
        self.helpframe = LabelFrame(self.master, font='Times 15', text='Help and Information Page', width=900, height=400, bd=10, fg='white', bg='grey')
        self.helpframe.place(x=45, y=40)


        def HelpPage():
            for widget in self.HelpList.winfo_children():
                widget.destroy()
            one = Label(self.HelpList, text = "********************************* INFORMATION *********************************\n \
                                                       \n► Function: The function of this system is to help users manage their tasks. It is simple and easy to use \
                                                    \n In general, it allows users to input their tasks into the system and mark them as completed by clicking the checkbox.\
                                                    \n\n► Purpose: The purpose of this system is to provide users with a simple and efficient way to manage \
                                                    \n and track their tasks ensuring they stay organized and productive. \
                                                    \n\n► Importance: This system is important because it streamlines task management, \
                                                    \n allowing users to prioritize, track progress, and stay focused on completing their tasks in a timely manner.\
                                                    \n\n► Brief Overview: This system is designed to help users input and manage tasks with ease. \
                                                    \n It offers a user-friendly interface where tasks can be marked as complete by simply checking a checkbox, \
                                                    \n making it a practical tool for both personal and professional use.", font='Times 13', fg='white', bg='grey', justify='left')
            one.place(x=1, y=1)
            
        def ButtonTask():
            for widget in self.HelpList.winfo_children():
                widget.destroy()
            two = Label(self.HelpList, text = "************************************ HELP ************************************** \
                                                        \nThe Buttons: \
                                                        \n\nAdd Task: - To add new task, click on the 'Add Task' Button. Just don't forget to input the fields first for smooth run! \
                                                        \n\nUpdate Task - To update an existing task, select the task from your task list and click on the 'Update Task' button. \
                                                        \nYou can then modify the task details. \
                                                        \n\nDisplay Task - This will just display the task you input.\
                                                        \n\nDelete Task - Delete the task", font='Times 13', fg='white', bg='grey', justify='left')
            two.place(x=1, y=1)
            
        def SDG():
            for widget in self.HelpList.winfo_children():
                widget.destroy()
            three = Label(self.HelpList, text = "************************************* SDG **************************************\
                                                        \n\nWhat SDG is this project? \
                                                        \n\nSDG 4: Quality Education: \
                                                        \n→The system helps users manage educational tasks, such as assignments, projects, and more.\
                                                        \n→ By organizing and prioritizing tasks, it enables users to stay on track with their learning goals, contributing to better \
                                                        \noutcomes in education.\
                                                        \n\nSDG 8: Decent Work and Economic Growth: \
                                                        \n→ The system can also support users in managing work-related tasks, ensuring productivity and efficiency in their \
                                                        \nprofessional roles. \
                                                        \n→ Tasks could be categorized by work objectives, helping users stay focused on career growth and meeting work \
                                                        \ndeadlines.", font='Times 13', fg='white', bg='grey', justify='left')
            three.place(x=1, y=1)

        def Exit():
            self.master.destroy()
        
        self.HelpList = Frame(self.helpframe, width=825, height=320, bg='grey')
        self.HelpList.place(x=4, y=3)
        
        self.Instruc = Label(self.HelpList, text = "Hello, there! This is the Task Management System's Help and Information Page \
                                                    \n\n To Provide you an overview of the project, there is a clickable button below containing some of the information including the uses of the \
                                                    \n program. In this very home page of the information page, there is a clickable button containing the following: \
                                                    \n\n ► Information ** Contains the information or overview of the program \
                                                    \n\n ► Help ** Contains how to use the button and what does it do in the program \
                                                    \n\n ► SDG ** Short-explanation of the SDG", font='Times 12', fg='white', bg='grey', justify='left')
        self.Instruc.place(x=1, y=1)

        self.InfoButton = ttk.Button(self.helpframe, text = 'Information', command = HelpPage)
        self.InfoButton.place(x=250, y=330)

        self.HelpButton = ttk.Button(self.helpframe, text = 'Help', command = ButtonTask)
        self.HelpButton.place(x=330, y=330)
        
        self.SDGOverview = ttk.Button(self.helpframe, text = 'SDG Overview', command = SDG)
        self.SDGOverview.place(x=410, y=330)
        
        self.HelpExit = ttk.Button(self.helpframe, text = 'Exit', command = Exit)
        self.HelpExit.place(x=498, y=330)
    

master = Tk()
app = MainWindow(master)
master.mainloop()