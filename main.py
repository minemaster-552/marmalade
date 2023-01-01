import tkinter as tk
from tkinter import ttk
from pygments.lexers.python import PythonLexer
from chlorophyll import CodeView
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

version = "0.0.2"

class Window(tk.Tk):
    def __init__(self, windowname:str=f"Marmalade v{version}"):
        super().__init__()
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()

        self.w = int(self.ws / 2)
        self.h = int(self.hs / 2)
        self.x = int((self.ws/2) - (self.w/2))
        self.y = int((self.hs/2) - (self.h/2))

        self.title(windowname)
        self.geometry(f"{self.w}x{self.h}+{self.x}+{self.y}")

        self.menubar = tk.Menu(self)

        self.filemenu = tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="New",command=None)
        self.filemenu.add_command(label="Save",command=None)
        self.filemenu.add_command(label="Load",command=None)
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.menubar.add_command(label="Exit",command=self.quit)

        self.config(menu=self.menubar)


        self.tabs = ttk.Notebook(self)

        self.code_edit = tk.Frame(self.tabs)
        self.actor_edit = tk.Frame(self.tabs)
        self.game_edit = tk.Frame(self.tabs)
        
        # Code Edit Frame
        self.editor = CodeView(self.code_edit, lexer=PythonLexer,color_scheme="ayu-dark")
        self.editor.pack(expand=True,fill=tk.BOTH)

        # Actor Edit Frame
        # self.add_button = tk.Button(self.actor_edit,text="Click Me!")
        self.actors = ttk.Treeview(self.actor_edit)
        self.actors.heading("#0",text="Actors",anchor=tk.W)
        self.actors.pack(expand=True,fill=tk.BOTH)

        self.tabs.add(self.code_edit, text="Code")
        self.tabs.add(self.actor_edit, text="Actors")
        self.tabs.add(self.game_edit, text="Game")
        self.tabs.pack(expand=True,fill=tk.BOTH)


if __name__ == "__main__":
    app = Window()
    app.mainloop()