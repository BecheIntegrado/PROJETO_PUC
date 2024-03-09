import tkinter as tk
from tkinter import messagebox

class TelaTurno(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cartão Ponto")
        self.state("zoomed")

        self.label = tk.Label(self, text="Cartão Ponto")
        self.label.pack(pady=10)

        self.btnCadVolta = tk.Button(self, text="Voltar", command=self.voltaMenu)
        self.btnCadVolta.pack(pady=10)

    def voltaMenu(self):
        self.destroy()
        self.master.deiconify()