import tkinter
from tkinter import ttk
import sv_ttk


root = tkinter.Tk()
root.geometry("150x150")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x_offset = (window.winfo_screenwidth() - width) // 2
    y_offset = (window.winfo_screenheight() - height) // 2
    window.geometry(f"+{x_offset}+{y_offset}")



def navigateFile():
    root.destroy()
    import main

button = ttk.Button(root, text="Hi", command=navigateFile)
button.grid(row=0, column=0, padx=10, pady=10)

center_window(root)
sv_ttk.set_theme("dark")

root.mainloop()