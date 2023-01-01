import tkinter as tk

version = "0.0.1"

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

        self.label = tk.Label(self,text="Marmalade: A python-based game engine")
        self.label.pack()


if __name__ == "__main__":
    app = Window()
    app.mainloop()