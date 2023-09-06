import tkinter as tk
from tkinter import messagebox
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.task_list = []
        
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.task_display = tk.Listbox(root, width=40)
        self.task_display.pack(pady=40)
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()
        
        self.load_tasks()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.append(task)
            self.task_display.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
            
    def remove_task(self):
        selected_index = self.task_display.curselection()
        if selected_index:
            index = selected_index[0]
            del self.task_list[index]
            self.task_display.delete(index)
            self.save_tasks()
            
    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.task_list:
                f.write(task + "\n")
                
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.read().splitlines()
            for task in tasks:
                self.task_list.append(task)
                self.task_display.insert(tk.END, task)
        except FileNotFoundError:
            pass
        
if __name__ == "__main__":
    root = tk.Tk()
    root["bg"]= "grey"
    root.geometry("850x450")
    app = TodoApp(root)
    root.mainloop()
