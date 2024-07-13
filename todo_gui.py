import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.id}. {self.description} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1

    def remove_task(self, id):
        self.tasks = [task for task in self.tasks if task.id != id]

    def complete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                task.mark_complete()

    def get_all_tasks(self):
        return self.tasks

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = ToDoList()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark Task as Complete", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.refresh_button = tk.Button(root, text="Refresh Tasks", command=self.refresh_tasks)
        self.refresh_button.pack(pady=5)

    def add_task(self):
        description = self.entry.get()
        if description:
            self.todo_list.add_task(description)
            self.entry.delete(0, tk.END)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task description.")

    def remove_task(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            task_id = int(selected_task.split('.')[0])
            self.todo_list.remove_task(task_id)
            self.refresh_tasks()
        except:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def complete_task(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            task_id = int(selected_task.split('.')[0])
            self.todo_list.complete_task(task_id)
            self.refresh_tasks()
        except:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.get_all_tasks():
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

