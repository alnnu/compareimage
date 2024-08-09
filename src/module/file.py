from tkinter import filedialog
import os

class File:
    def readFile(self):
        path = filedialog.askdirectory()
        itens = []
        if path:
            for item in os.listdir(path):
                itens.append(item)

        return itens