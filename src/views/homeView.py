import tkinter
from tkinter import *
from tkinter import ttk

from src.module.file import File
from src.views.errorView import Error


class Home(Tk):
    def __init__(self):
        super().__init__()
        self.title("home")

        self.frame = ttk.Frame(self, padding="12 12 12 12")
        self.frame.grid(column=1, row=1)

        ttk.Button(self.frame, text="abrir pasta", command=self.read).grid(column=1, row=1, sticky=(E, W))
        ttk.Button(self.frame, text="comparar", command=self.coparar).grid(column=2, row=1, sticky=(E, W))

        self.folder_contents = tkinter.Listbox(self.frame, selectmode=tkinter.SINGLE)
        self.folder_contents.grid(column=1, row=2, columnspan=2, sticky=(E, W))

        # Create a scrollbar for the Listbox
        scrollbar = tkinter.Scrollbar(self.folder_contents, orient=tkinter.VERTICAL)
        scrollbar.config(command=self.folder_contents.yview)
        self.folder_contents.config(yscrollcommand=scrollbar.set)
        self.addPading()
        self.mainloop()

    def read(self):
        fileModule = File()

        files = fileModule.readFile()

        self.folder_contents.delete(0, tkinter.END)

        for item in files:
            self.folder_contents.insert(tkinter.END, item)

    def clean_frame(self):
        for itens in self.frame.winfo_children():
            itens.destroy()

    def coparar(self):
        total_files = self.folder_contents.size()

        if total_files > 0:
            ttk.Label(self.frame, text="Total repetidas:").grid(column=1, row=3, sticky=(W, E))
            ttk.Label(self.frame, text="0").grid(column=2, row=3, sticky=(W, E))
            ttk.Button(self.frame, text="baixar fotos").grid(column=1, row=4, columnspan=2, sticky=(E, W))
            self.addPading()
        else:
            Error("Nem uma foto encontrada")



    def addPading(self):
        for child in self.frame.winfo_children():
            child.grid_configure(padx=6, pady=6)