import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

label = ttk.Label(window, text='Ejercicio 10.1')
label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)

lista = ['Item #1', 'Item #2', 'Item #3', 'Item #4']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
listbox.grid(column=0, row=1, sticky=tkinter.W)

window.mainloop()
