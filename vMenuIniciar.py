import tkinter as tk
from tkinter import messagebox
from vTelaDepartamento import *
from vTelaFuncionario import *
from vTelaTurno import *

class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Funcionário")
        self.state("zoomed")
        self.configure(bg="#4F4F4F")
        self.tela_inicial = TelaMenu(self)
        self.tela_inicial.pack(expand=True, fill='both')


class TelaMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#4F4F4F")  # Cor de fundo do frame
        self.master = master

        self.label = tk.Label(self, text="MENU", font=("Arial", 20), bg="#4F4F4F", fg="white")  # Cor de fundo e texto
        self.label.pack(pady=(50, 10))

        self.btnCadFunc = tk.Button(self, text="Cadastro de Funcionário", command=self.fCadFunc, width=20)  # Botão sem cor
        self.btnCadFunc.pack(pady=10)

        self.btnCadTurno = tk.Button(self, text="Cartão Ponto", command=self.fCadTurno, width=20)
        self.btnCadTurno.pack(pady=10)

        self.btnCadDep = tk.Button(self, text="Cadastro de Departamento", command=self.fCadDep, width=20)
        self.btnCadDep.pack(pady=10)

        self.btnSair = tk.Button(self, text="Sair", command=self.fSair, width=20)
        self.btnSair.pack(pady=10)

    def fCadFunc(self):
        self.master.withdraw()
        TelaCadFunc(self.master)

    def fCadTurno(self):
        self.master.withdraw()
        TelaTurno(self.master)

    def fCadDep(self):
        self.master.withdraw()
        TelaDepartamento(self.master)

    def fSair(self):
        self.master.quit()

app = Aplicacao()
app.mainloop()