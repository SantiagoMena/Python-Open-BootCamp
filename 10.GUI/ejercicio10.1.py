import tkinter
from tkinter import ttk

class Window:
    seleccionado = None
    def main(self):
        window = tkinter.Tk()

        window.columnconfigure(0, weight=1)
        window.columnconfigure(0, weight=3)

        label = ttk.Label(window, text='Ejercicio 10.1')
        label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)

        self.seleccionado = tkinter.StringVar()
        r1 = ttk.Radiobutton(window, text='Botón #1', value='Botón #1', variable=self.seleccionado)
        r2 = ttk.Radiobutton(window, text='Botón #2', value='Botón #2', variable=self.seleccionado)
        r3 = ttk.Radiobutton(window, text='Botón #3', value='Botón #3', variable=self.seleccionado)
        r4 = ttk.Radiobutton(window, text='Botón #4', value='Botón #4', variable=self.seleccionado)
        r5 = ttk.Radiobutton(window, text='Botón #5', value='Botón #5', variable=self.seleccionado)

        r1.grid(column=0, row=1, padx=5, pady=5)
        r2.grid(column=0, row=2, padx=5, pady=5)
        r3.grid(column=0, row=3, padx=5, pady=5)
        r4.grid(column=0, row=4, padx=5, pady=5)
        r5.grid(column=0, row=5, padx=5, pady=5)

        def reiniciar(event):
            self.seleccionado.set('')

        botonReiniciar = ttk.Button(window, text='Reiniciar')
        botonReiniciar.grid(column=0, row=6, padx=5, pady=5)
        # botonReiniciar.pack()
        botonReiniciar.bind('<Button-1>', reiniciar)

        window.mainloop()

window = Window()
window.main()