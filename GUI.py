from tkinter import *
from random import choice

App = Tk()
App.title("My App")
App.geometry("400x200")
App.configure(background='black')

lbl = Label(App,text="Welcome to my first python GUI App", borderwidth=4, bg='black', fg='white')

def click():
    lst = ["Have a nice day", "You clicked!", "Wazzzuuuuupppp!", "OUCH!"]
    lbl.configure(text=choice(lst))

btn = Button(App, text="Click me", command=click)

# btn.grid(row=0, column=0, padx=10, pady=10)
# lbl.grid(row=1, column=0, padx=10, pady=10)
Label(App, text='', bg='black').pack()
btn.pack()
Label(App, text='', bg='black').pack()
lbl.pack()

App.mainloop()
