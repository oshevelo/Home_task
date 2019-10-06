from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Calculator")

bttn = ["="]
r = 1
c = 0
for i in bttn:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 20).grid(row=r, column=c)

calc_entry = Entry(root, width=45)
calc_entry.grid(row=0, column=0, columnspan=5)

#логика калькулятора
def calc(key):
    global memory
    if key == "=":
#исключение написания слов
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
#исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
# " = "
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

root.mainloop()