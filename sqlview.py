import tkinter
from tkinter import ttk
import mysql.connector
import sv_ttk


root = tkinter.Tk()
root.title("Upperbody Workout")
    


connection = mysql.connector.connect(host='localhost', user='root', password = '', port='3306', database='workout')
conn = connection.cursor()

def table():
    conn.execute('SELECT * FROM upperbody')
    rows = conn.fetchall()

    table1 = ttk.Treeview(root, columns=[str(i) for i in range(len(rows[0]))], show='headings')

    #table1 = ttk.Treeview(root)

    columns = [col[0] for col in conn.description]

    table1["columns"] = columns

    for col in columns:
        table1.heading(col, text=col)

    for row in rows:
        table1.insert("", "end", values=row)

    style = ttk.Style(root)
    style.configure("Treeview", cellanchor="center")


    table1.pack(expand=True, fill="both")



sv_ttk.set_theme("dark")

table()

root.mainloop()