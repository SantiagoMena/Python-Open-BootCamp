import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text='Hola Mundo!', bg='blue', fg='white')
label_saludo.pack(ipadx=30, ipady=30, expand=True)

label_adios = tkinter.Label(window, text='Adios Mundo!', bg='white', fg='black')
label_adios.pack(ipadx=50, ipady=100, fill='both')

window.mainloop()