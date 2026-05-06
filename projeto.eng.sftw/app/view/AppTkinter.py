import tkinter as tk
from view.camposaplicativo import Campos_Aplicativo 

class AppTkinter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App de Gerenciamento de Usuários")
        self.geometry("400x500")
        self.option_add("*Font", "Arial 10") 

        self.campos = Campos_Aplicativo(self)

    def run_app(self):
        self.mainloop()