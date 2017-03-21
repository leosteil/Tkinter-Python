import tkinter as tk
from escreveArquivo import EscArqView

class MainView:
    def __init__(self, master):
        self.master = master

        self.container1 = tk.Frame(self.master)
        self.button1 = tk.Button(self.container1, text = 'Escrever no arquivo', width = 25, command = self.new_window)
        self.button1.pack()
        self.container1.pack()

        self.container1 = tk.Frame(self.master)
        self.button1 = tk.Button(self.container1, text = 'Remover Classe', width = 25, command = self.new_window)
        self.button1.pack()
        self.container1.pack()


        self.container1 = tk.Frame(self.master)
        self.button2 = tk.Button(self.container1, text = "Importar", width = 25, command = self.new_window)
        self.button2.pack()
        self.container1.pack()

    def new_window(self):
        #self.newWindow
        self.newWindow = tk.Toplevel(self.master)
        self.app = EscArqView(self.newWindow)


root = tk.Tk()
MainView(root)
root.mainloop()