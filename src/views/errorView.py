from tkinter import *
from tkinter import ttk



class Error(Tk):
    def __init__(self, error):
        super().__init__()
        self.title("home")
        print(error)
        self.frame = ttk.Frame(self, padding="12 12 12 12")
        self.frame.grid(column=1, row=1)

        ttk.Label(self.frame, text=error).grid(column=1, row=1, sticky=(W, E))

        ttk.Button(self.frame, text="voltar", command=self.destroy).grid(column=1, row=2, sticky=(W,E))
        self.addPading()
        self.mainloop()




    def addPading(self):
        for child in self.frame.winfo_children():
            child.grid_configure(padx=6, pady=6)