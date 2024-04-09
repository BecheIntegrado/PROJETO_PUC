import tkinter as tk
from tkinter import messagebox
from control.cControlFunc import *

class TelaDepartamento(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Cadastro de Departamento")
        self.state("zoomed")

        self.label_titulo = tk.Label(self, text="Cadastro de Departamento", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=20)

        self.frame_campos = tk.Frame(self)
        self.frame_campos.pack(padx=20, pady=10)

        self.label_nomeDep = tk.Label(self.frame_campos, text="Nome Departamento:", font=("Arial", 14))
        self.label_nomeDep.grid(row=1, column=0, pady=5)
        self.entry_nomeDep = tk.Entry(self.frame_campos, font=("Arial", 14))
        self.entry_nomeDep.grid(row=1, column=1, pady=5)

        self.btn_salvar = tk.Button(self.frame_campos, text="Salvar", command=self.cadDepartamento)
        self.btn_salvar.grid(row=2, column=0, pady=5, padx=5)

        self.btn_limpar = tk.Button(self.frame_campos, text="Limpar", command=self.limparCampos)
        self.btn_limpar.grid(row=2, column=1, pady=5, padx=5)

        self.btn_voltar = tk.Button(self.frame_campos, text="Voltar", command=self.voltaMenu)
        self.btn_voltar.grid(row=2, column=2, pady=5, padx=5)

    def cadDepartamento(self):
        nm_dep = self.entry_nomeDep.get()

        if not nm_dep:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        salvaDepartamento = cDepartamento(nm_dep=nm_dep, cd_dep = '')
        salvaDepartamento.setDepartamento()

        self.limparCampos()

        messagebox.showinfo("Sucesso", "Departamento cadastrado com sucesso!")

    def voltaMenu(self):
        self.destroy()
        self.master.deiconify()
        self.master.state("zoomed")

    def limparCampos(self):
        self.entry_nomeDep.delete(0, tk.END)
